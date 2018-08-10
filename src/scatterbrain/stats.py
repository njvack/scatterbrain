import os

import pandas as pd
import statsmodels
import statsmodels.api as sm
import numpy as np
import nibabel

from . import settings


def papaya_coords_to_numpy_coords(image, papaya_coords):
    # papaya_coords should be a tuple (x, y, z)
    papaya_coords_ar = np.array(papaya_coords)
    shapearr = np.array(image.shape[0:3])
    return tuple((shapearr - 1) - papaya_coords_ar)


def get_voxel_values(image, papaya_coords):
    numpy_coords = papaya_coords_to_numpy_coords(image, papaya_coords)
    return image.get_data()[numpy_coords]


def regress_for_scatterplot(image_name, df_name, papaya_coords):
    # For now we're gonna hardwire the column
    image = load_image(image_name)
    df = load_df(df_name)
    df['__CONST'] = 1
    y = get_voxel_values(image, papaya_coords)
    x = df[['SRS_RAW_TOTAL', '__CONST']]
    model = sm.OLS(y, x)
    result = model.fit()
    return result

    # return dict(
    #     points=points.tolist(),
    #     stats_diagnostics=self.diagnostics_list(),
    #     all_point_data=all_point_data.tolist(),
    #     all_point_cols=self._all_point_cols(self.include_cols),
    #     regression_line=regression_line,
    #     group_list=[],
    #     x_label='SRS_RAW_TOTAL',
    #     y_label=f'Voxel {papaya_coords}',
    #     model_type='OLS')



def load_image(image_name):
    image_path = os.path.join(settings.STATS_INPUT_DIR, 'y_ts', image_name)
    return nibabel.load(image_path)


def load_df(df_name):
    df_path = os.path.join(settings.STATS_INPUT_DIR, 'x_mat', df_name)
    return pd.read_csv(df_path)
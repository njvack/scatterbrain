import os

import pandas as pd
import statsmodels
import statsmodels.api as sm
import numpy as np
import nibabel

from . import settings

import logging
logger = logging.getLogger(__name__)


def papaya_coords_to_numpy_coords(image, papaya_coords):
    # papaya_coords should be a tuple (x, y, z)
    return tuple(np.rint(papaya_coords).astype(int))


def get_voxel_values(image, papaya_coords):
    numpy_coords = papaya_coords_to_numpy_coords(image, papaya_coords)
    return image.get_data()[numpy_coords]


def build_and_fit_model(image_key, df_key, papaya_coords):
    # For now we're gonna hardwire the column
    image = load_image(image_key)
    df = load_df(df_key)
    df['__CONST'] = 1
    y = get_voxel_values(image, papaya_coords)
    x = df[['__CONST', 'SRS_RAW_TOTAL']]
    logger.debug(y)
    logger.debug(x)
    model = sm.OLS(y, x)
    result = model.fit()
    return result


def regress_for_scatterplot(image_key, df_key, papaya_coords, world_coords):
    result = build_and_fit_model(image_key, df_key, papaya_coords)
    points = np.column_stack((
        np.arange(result.nobs),
        result.model.exog[:, 1],
        result.model.endog,
        np.ones_like(result.model.endog),
        np.zeros_like(result.model.endog)
    ))
    regression_line = {
        'const': result.params[0],
        'slope': result.params[1]
    }
    diags = [{
        'data': [['n', int(result.nobs)]]
    }]
    return dict(
        points=points.tolist(),
        stats_diagnostics=diags,
        # all_point_data=all_point_data.tolist(),
        # all_point_cols=self._all_point_cols(self.include_cols),
        regression_line=regression_line,
        group_list=[],
        x_label='SRS_RAW_TOTAL',
        y_label=f'Voxel {world_coords}',
        model_type='OLS')


def load_image(key):
    image_name = f'{key}.nii.gz'
    image_path = os.path.join(settings.STATS_INPUT_DIR, 'y_ts', image_name)
    return nibabel.load(image_path)


def load_df(key):
    df_name = f'{key}.csv'
    df_path = os.path.join(settings.STATS_INPUT_DIR, 'x_mat', df_name)
    return pd.read_csv(df_path)

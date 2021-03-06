import flask
from flask import Flask, render_template, request, jsonify

import json

from . import stats

app = Flask(__name__)


logger = app.logger
stats.logger = app.logger

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot/<image_key>/<csv_key>')
def plot(image_key, csv_key):
    logger.info(f'Gonna plot for image {image_key}, csv {csv_key}')
    df = stats.load_df(csv_key)
    return render_template(
        'plot.html',
        image_key=image_key,
        csv_key=csv_key,
        columns=list(df.columns))


@app.route('/regress_voxel/<image_key>/<csv_key>')
def regress_voxel(image_key, csv_key):
    a = request.args
    logger.debug(a)
    papaya_coords = (
        float(a.get('x', 0)),
        float(a.get('y', 0)),
        float(a.get('z', 0))
    )
    world_coord_str = a.get('world_coords')
    logger.info(f"I am in regress_voxel, gonna regress {request.args}")
    return jsonify(stats.regress_for_scatterplot(
        image_key, csv_key, papaya_coords, world_coord_str))

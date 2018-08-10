import flask
from flask import Flask, render_template, request, jsonify

import json

from . import stats

app = Flask(__name__)


logger = app.logger


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot/<image_key>/<csv_key>')
def plot(image_key, csv_key):
    logger.info(f'Gonna plot for image {image_key}, csv {csv_key}')
    return render_template('plot.html', image_key=image_key, csv_key=csv_key)


@app.route('/regress_voxel/<image_key>/<csv_key>')
def regress_voxel(image_key, csv_key):
    a = request.args
    papaya_coords = (
        a.get('x', 0),
        a.get('y', 0),
        a.get('z', 0)
    )
    logger.info(f"I am in regress_voxel, gonna regress {request.args}")
    return jsonify(stats.regress_for_scatterplot(
        image_key, csv_key, papaya_coords))

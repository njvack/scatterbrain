import flask
from flask import Flask, render_template, url_for, request

import json

from . import stats

app = Flask(__name__)


logger = app.logger


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/regress_voxel')
def regress_voxel():
    logger.info(f"I am in regress_voxel, gonna regress {request.args}")

    return json.dumps(request.args)
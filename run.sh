#!/bin/bash

export FLASK_DEBUG=1
export FLASK_ENV=develpoment
export FLASK_APP=src/scatterbrain/server.py
flask run
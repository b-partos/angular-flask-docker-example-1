#!/bin/bash
export FLASK_APP=./src/main.py
#export FLASK_RUN_PORT=8000
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0


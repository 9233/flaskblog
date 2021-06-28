#!/bin/bash
export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
/opt/py3/bin/flask run --host=0.0.0.0 --port=5002

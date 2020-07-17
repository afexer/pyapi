#!/usr/bin/env python
# - *- coding: utf- 8 - *-
import os
import sys
import logging

from celery import Celery
celery = Celery(broker='redis://localhost:6379/0')

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
os.environ['BASE_PATH'] = BASE_PATH

activate_this = BASE_PATH+'venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, BASE_PATH)

from app import app

application = app


"""WSGI entry point for WEL Inventory.

`python app.py` sets the database up inside its `if __name__ == '__main__'`
block. A production server (gunicorn, uWSGI, PythonAnywhere) imports the
module instead, so that block never runs and the app would start against an
empty database.

This module runs the same setup at import time and then exposes `app`, so any
WSGI server can serve it:

    gunicorn wsgi:app
"""
from app import app, init_db

with app.app_context():
    init_db()

# `app` is what the WSGI server serves.
application = app

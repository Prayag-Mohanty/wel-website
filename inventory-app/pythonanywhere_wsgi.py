"""Paste this into the WSGI configuration file on PythonAnywhere.

Web tab -> "WSGI configuration file" -> replace everything in it with the
contents of this file, change USERNAME on the PROJECT line, and Reload.

Two things here are not optional, and both are the reason a Flask app that
runs fine locally fails on PythonAnywhere:

1. The server runs this file from a working directory that is NOT your project
   folder. `load_dotenv()` with no argument looks in the *current* directory,
   so it would find nothing and the app would start with its fallback secret
   key and no admin account. Hence the absolute path.

2. The .env has to be loaded BEFORE `wsgi` is imported. app.py reads its
   settings at import time, so loading them afterwards would be too late.

This file is only used on PythonAnywhere. Running locally, or under Docker,
uses wsgi.py directly.
"""
import os
import sys

# ---- change USERNAME to your PythonAnywhere username ----------------------
PROJECT = '/home/USERNAME/wel-website/inventory-app'
# ---------------------------------------------------------------------------

if PROJECT not in sys.path:
    sys.path.insert(0, PROJECT)

from dotenv import load_dotenv                       # noqa: E402

load_dotenv(os.path.join(PROJECT, '.env'))

from wsgi import application                         # noqa: E402,F401

# `application` is what PythonAnywhere serves. Importing it has already
# created the database tables, upgraded an older database if needed, and
# seeded the admin account from .env - see wsgi.py.

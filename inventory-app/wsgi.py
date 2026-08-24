"""WSGI entry point for WEL Inventory.

`python app.py` creates the database tables and the admin account inside its
`if __name__ == '__main__'` block.  A production server (gunicorn, uWSGI,
PythonAnywhere) imports the module instead, so that block never runs and the
app would start against an empty database.

This module does that setup at import time and then exposes `app`, so any WSGI
server can serve it:

    gunicorn wsgi:app

app.py itself is left exactly as written.
"""
from app import ADMIN_EMAIL, ADMIN_PASSWORD, User, app, db

with app.app_context():
    db.create_all()
    if ADMIN_EMAIL and not User.query.filter_by(email=ADMIN_EMAIL).first():
        admin = User(email=ADMIN_EMAIL, is_admin=True)
        admin.set_password(ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()
        print("Admin account created: %s" % ADMIN_EMAIL)

# `app` is what the WSGI server serves.
application = app

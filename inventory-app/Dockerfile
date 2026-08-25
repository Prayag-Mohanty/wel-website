# WEL Inventory - the Flask app, packaged so it runs the same anywhere.
#
#   docker compose up -d inventory      (from the repository root)
#
# The database lives in /app/instance, which compose mounts as a named volume,
# so stock and team registrations survive rebuilds and restarts.

FROM python:3.12-slim

# Keeps Python from writing .pyc files into the mounted volume, and makes log
# output appear immediately rather than sitting in a buffer.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencies first, so changing application code does not re-install them.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# Run as a non-root user, and give it ownership of the database directory.
RUN useradd --create-home --uid 10001 wel \
    && mkdir -p /app/instance \
    && chown -R wel:wel /app
USER wel

EXPOSE 5000

# wsgi:app rather than app:app - app.py creates its tables inside
# `if __name__ == '__main__'`, which a WSGI server never runs. See wsgi.py.
CMD ["gunicorn", "wsgi:app", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "2", \
     "--timeout", "60", \
     "--access-logfile", "-"]

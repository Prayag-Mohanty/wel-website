# The WEL website, packaged as a self-contained web server.
#
#   docker compose up -d site      ->  http://localhost:8080
#
# Two stages: the first runs the site generator, the second serves the result
# with nginx. The finished image carries no Python and no build tooling - just
# nginx and the generated files - so it is small and there is nothing extra to
# keep patched.

# ---- stage 1: generate the HTML -------------------------------------------
FROM python:3.12-slim AS build

WORKDIR /src
COPY . .

# Rebuild from source so the image can never drift from _src/, and fail the
# build if any internal link is broken.
RUN python _src/build.py | tee /tmp/build.log \
    && grep -q "All internal links resolve." /tmp/build.log \
    && mkdir -p /site \
    && cp *.html /site/ \
    && cp -r assets /site/ \
    && cp favicon.ico /site/ 2>/dev/null || true

# ---- stage 2: serve it ----------------------------------------------------
FROM nginx:alpine

COPY --from=build /site /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -q --spider http://localhost/ || exit 1

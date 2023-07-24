#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input --clear
cp -rf /app/static/. /static/
cp -rf /app/collected_static/. /static/
cd /app/data; wget https://git.io/GeoLite2-Country.mmdb

exec "$@"
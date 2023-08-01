#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input --clear
cp -rf /app/static/. /static/
cp -rf /app/collected_static/. /static/
wget https://git.io/GeoLite2-Country.mmdb -O /app/data/GeoLite2-Country.mmdb

exec "$@"
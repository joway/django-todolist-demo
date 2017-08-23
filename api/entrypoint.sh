#!/usr/bin/env bash
python manage.py migrate

uwsgi --chdir=/code \
      --module=config.wsgi:application \
      --master \
      --http-socket=0.0.0.0:8000 \
      --processes=1 \
      --harakiri=30 \
      --max-requests=500

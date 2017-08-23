#!/usr/bin/env bash
MODE=${MODE:-API}

if  [ $MODE == "STATIC" ]; then
    echo "start nginx on port 80"
    nginx -g "daemon off;"
    exit 0
fi

python manage.py migrate

uwsgi --chdir=/code \
      --module=config.wsgi:application \
      --gevent 100 \
      --master \
      --processes 1 \
      --disable-logging \
      --enable-threads \
      --single-interpreter \
      --http-keepalive \
      --post-buffering 32768 \
      --http=0.0.0.0:8000 \
      --harakiri-verbose \
      --harakiri=30

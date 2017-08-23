FROM python:3.6.1-slim

MAINTAINER joway wang <joway.w@gmail.com>
ENV TZ Asia/Shanghai

RUN apt update \
    && apt install -y build-essential libmysqlclient-dev mysql-client nginx \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code/cache
WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install -r ./requirements.txt

COPY ./.deploy/nginx.conf /etc/nginx/sites-enabled/default
COPY . /code

RUN python manage.py collectstatic --noinput

EXPOSE 8000
EXPOSE 80

ENTRYPOINT ./entrypoint.sh

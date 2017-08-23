FROM python:3.6.1-slim

MAINTAINER Joway Wang <i@joway.io>
ENV TZ Asia/Shanghai

RUN apt update \
    && apt install -y build-essential libmysqlclient-dev mysql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install -r ./requirements.txt

COPY . /code

EXPOSE 8000

ENTRYPOINT ./entrypoint.sh

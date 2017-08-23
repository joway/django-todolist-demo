FROM node:7.10.0
MAINTAINER joway wang <joway.w@gmail.com>
ENV TZ Asia/Shanghai
ENV NODE_ENV 'production'

RUN mkdir -p /app
WORKDIR /app
RUN apt update && apt install -y nginx && apt-get autoclean

COPY package.json /app/
RUN npm install
COPY . /app
COPY ./config/nginx.conf /etc/nginx/sites-enabled/default

RUN npm run build && rm -rf node_modules
EXPOSE 80

ENTRYPOINT nginx -g "daemon off;"

FROM python:3.8
LABEL maintainer="REBOUÇAS, Daniel Nogueira <danielnreboucas@hotmail.com>"

WORKDIR /lewi-web-api
ADD . /lewi-web-api

RUN pip install -r requirements.txt

EXPOSE 8390

CMD ["uwsgi", "app.ini"]
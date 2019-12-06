FROM python:3-buster

COPY . /opt/webnmap

WORKDIR /opt/webnmap

RUN pip install -r requirements.txt

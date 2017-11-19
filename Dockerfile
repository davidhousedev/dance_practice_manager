FROM python:3

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
ADD . .

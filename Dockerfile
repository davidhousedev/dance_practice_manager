FROM python:3

EXPOSE 8000

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
ADD . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential libldap2-dev libsasl2-dev netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/code/entrypoint.sh"]

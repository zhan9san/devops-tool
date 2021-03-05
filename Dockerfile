FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential libldap2-dev libsasl2-dev netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

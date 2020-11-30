#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DJANGO_DB_HOST $DJANGO_DB_PORT; do
  sleep 1
done

echo "PostgreSQL started"

exec "$@"

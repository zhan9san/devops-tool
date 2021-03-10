# devops-tool

## Development environment

Run the following comands in three different terminals

```bash script
docker-compose up --build
docker-compose exec web celery -A DevOpsTool worker -l info
docker-compose exec web celery flower -A DevOpsTool -l debug
```

## Production environment

Keep `.env.prod` out of version control for a real-world scenario.

## Define image version tag

If `DEVOPS_TOOL_WEB_VERSION` and `DEVOPS_TOOL_NGINX_VERSION` are not defined,
`latest` will be used.

```shell script
export DEVOPS_TOOL_WEB_VERSION=0.0.1
export DEVOPS_TOOL_NGINX_VERSION=0.0.1
```

## Build services

```shell script
docker-compose -f docker-compose.prod.yml build
```

## Pushes service images to [Docker Hub](https://hub.docker.com/)

```shell script
docker-compose -f docker-compose.prod.yml push
```

## Create and start containers

```shell script
docker-compose -f docker-compose.prod.yml up -d
```

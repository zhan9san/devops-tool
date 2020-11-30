# devops-tool

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

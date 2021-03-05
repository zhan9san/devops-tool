FROM python:3.9-alpine3.12

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN echo -e "https://mirrors.aliyun.com/alpine/v3.12/main/\nhttps://mirrors.aliyun.com/alpine/v3.12/community" \
    > /etc/apk/repositories
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openldap-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

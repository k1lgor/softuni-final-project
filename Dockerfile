# temp stage
# pull official base image
FROM python:3.11-alpine as builder

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apk update && apk add postgresql-dev postgresql-client gcc python3-dev musl-dev

# install project dependencies
COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps -r /tmp/requirements.txt -w /app/wheels


# final stage
# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /app

# install project dependencies
COPY --from=builder /app/wheels /tmp/wheels
COPY requirements.txt /app/
RUN pip install --no-cache -r /app/requirements.txt -f /tmp/wheels && rm -rf /tmp/*

# copy entrypoint.sh
COPY entrypoint.sh /app/
# RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy project files
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

FROM python:3.7-alpine
MAINTAINER mohamed(cboy)

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /first_motors
WORKDIR /first_motors

RUN  adduser  -D user
RUN chown -R user /first_motors
USER user




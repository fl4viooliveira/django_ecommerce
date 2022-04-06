FROM python:3.9.6-alpine3.14

ENV PROJECT_DIR=/opt/project

RUN true \
    && apk add --upgrade \
    && apk add \
      musl-dev \
      build-base \
      postgresql-dev \
      libffi-dev \
      jpeg-dev \
      zlib-dev \
      libjpeg

WORKDIR $PROJECT_DIR

COPY requirements.txt requirements.txt
COPY . .

RUN true \
    && python -m pip install --upgrade pip \
    && python -m pip install -r $PROJECT_DIR/requirements.txt

RUN mkdir -p $PROJECT_DIR/ecom/static
RUN python $PROJECT_DIR/manage.py migrate
RUN python $PROJECT_DIR/manage.py collectstatic
RUN gunicorn ecom.wsgi:application -c $PROJECT_DIR/ecom/gunicorn.py

EXPOSE 8000

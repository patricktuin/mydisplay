FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

RUN ./manage.py migrate
RUN ./manage.py collectstatic --no-input

CMD gunicorn openshift_django.wsgi -b 0.0.0.0:8000

EXPOSE 8000
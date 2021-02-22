FROM python:3.7.10-slim-stretch

LABEL maintainer="eleazar.yewa.harold@gmail.com"
#Ensure that Python outputs all log messages inside the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code
COPY . /code
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["/bin/bash", "./run.sh"]
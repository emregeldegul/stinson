FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY . /code/
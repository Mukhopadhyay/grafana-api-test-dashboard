FROM python:3.10-slim as builder

RUN apt update && apt -y --no-install-recommends install g++

# disabling pyc generation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /
RUN pip3 install -r requirements.txt

WORKDIR /src

COPY ./src .

RUN ls -al

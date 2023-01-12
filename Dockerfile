FROM python:3.10-slim

# RUN apt update && apt -y --no-install-recommends install g++

# disabling pyc generation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /
RUN pip3 install -r requirements.txt

# Setting working directory to src
WORKDIR /src

COPY ./src .

# Copying the start.sh
COPY ./start.sh .
RUN chmod +x ./start.sh

RUN ls -al

# Starting the server
CMD ["sh", "start.sh"]

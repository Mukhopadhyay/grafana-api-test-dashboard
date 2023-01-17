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
COPY ./grafana-init.sh .

# Setting execution permission
RUN chmod +x ./start.sh
RUN chmod +x ./grafana-init.sh

RUN ls -al

# Starting the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

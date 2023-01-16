#!/bin/sh

# Caveman wait for DB to get started
sleep 5

# Database migration
alembic revision -m "migration-script" --autogenerate
alembic upgrade head

# Start the server
# uvicorn app:app --reload --host 0.0.0.0 --port 8000
# gunicorn app:app --workers 2 --worker-class uvicorn.workers.UvicornWorkers --bind 0.0.0.0:8000 --daemon

# Grafana initialization
echo "Grafana initialization"
sleep 5
python grafana_init.py

# Scheduler
echo "API Scheduler"
sleep 5
nohup python scheduler.py > nohup.out &

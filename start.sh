#!/bin/sh

# Caveman wait for DB to get started
sleep 5

# Database migration
alembic revision -m "migration-script" --autogenerate
alembic upgrade head

# Grafana initialization
echo "Grafana initialization"
sleep 5
python grafana_init.py

# Scheduler
echo "API Scheduler"
sleep 5
python scheduler.py

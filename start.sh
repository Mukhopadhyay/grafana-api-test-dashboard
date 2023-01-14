#!/bin/sh

# Caveman wait for DB to get started
sleep 5

# Database migration
alembic revision -m "migration-script" --autogenerate
alembic upgrade head

# Start the server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
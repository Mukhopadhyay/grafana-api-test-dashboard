#!/bin/sh

# Wait for 10 seconds
sleep 10
echo "Done waiting!"

# Database migration
alembic revision -m "migration-script" --autogenerate
alembic upgrade head

# Start the server
uvicorn app:app --reload --host 0.0.0.0 --port 8000

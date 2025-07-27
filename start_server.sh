#!/bin/bash

# Start the Kotogram FastAPI server
echo "Starting Kotogram FastAPI server..."

# Activate virtual environment and start server
source .venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8080 --reload

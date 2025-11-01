#!/bin/bash
set -e
if [ "$ENV_MODE" = "local" ]; then
    echo "Running in local mode..."
    tail -f /dev/null
else
    echo "Running in Prod mode..."
    python uvicorn_config.py
fi
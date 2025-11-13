#!/bin/bash

set -e

# Create virtual environment
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

# Activate and install dependencies
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run mic listener service
python services/mic-listener.py "$@"
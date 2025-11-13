#!/bin/bash
set -e

# Create .venv if it doesn't exist
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

# Activate .venv
source .venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run the app
python main.py

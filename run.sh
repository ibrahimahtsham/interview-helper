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




echo "Select an option:"
echo "1) Run mic listener"
read -p "Enter choice [1]: " choice

case $choice in
	1|"")
		python services/mic-listener.py
		;;
	*)
		echo "Invalid option."
		;;
esac
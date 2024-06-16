#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests in parallel
pytest test_game.py &

# Run the main game in parallel
python main.py &

# Wait for all processes to finish
wait

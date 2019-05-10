#!/bin/bash
# Helper script that checks if the bot is running

# NOTE: This file is simply a reference of what you could use, it will not necessarily work in your own environment
if pgrep -f "Scheduler.py" >/dev/null
then
  echo "Running"
else
  echo "Stopped"
fi

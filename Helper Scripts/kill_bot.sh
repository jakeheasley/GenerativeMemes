#!/bin/bash
# Script that stops the bot from running and the deletes the crontab file that jumpstarts it

# NOTE: This file is simply a reference of what you could use, it will not necessarily work in your own environment
if pgrep -f "Scheduler.py" >/dev/null
then
  pkill -f Scheduler.py

export EDITOR="tee"
echo "" | crontab -e
fi  

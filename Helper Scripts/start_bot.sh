#!/bin/bash
# script that initializes the bot as a background process as well as creates a crontab file
# that runs run_again.sh every minute

# NOTE: This file is simply a reference of what you could use, it will not necessarily work in your own environment
cd GenerativeMemes/Prototype
nohup python3 Scheduler.py
export EDITOR="tee"
echo "* * * * *  ./run_again.sh" | crontab -e

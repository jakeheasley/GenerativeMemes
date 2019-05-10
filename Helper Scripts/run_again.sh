#!/bin/bash
# Script that checks if bot is running, and if not runs it again

# NOTE: This file is simply a reference of what you could use, it will not necessarily work in your own environment
if pgrep -f "Scheduler.py" >/dev/null
then
	echo "Running"
else
	cd GenerativeMemes/Prototype
	nohup python3 Scheduler.py
fi

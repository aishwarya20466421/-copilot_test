#!/usr/bin/env python3

import time

def get_uptime_seconds():
    try:
        with open("/proc/uptime", "r") as f:
            return float(f.readline().split()[0])
    except (FileNotFoundError, ValueError):
        return None

uptime_seconds = get_uptime_seconds()

if uptime_seconds is None:
    print("Uptime information is not available on this system.")
else:
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"System uptime: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")

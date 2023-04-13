"""
Author: Matthew Post
File: main.py
Description: This module simply prints the current time every 10 seconds forever
"""

import datetime
import time

if __name__ == "__main__":
    while True:
        print(f"The time is {datetime.datetime.now()}")
        time.sleep(10)

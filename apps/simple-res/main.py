"""
Author: Matthew Post
File: main.py
Description: This module is simply prints the current time every 10 seconds forever but the Argo
    `WorkflowTemplate` located in the `helm/` directory consumes an arbitrary resource in the cluster
"""

import datetime
import time

if __name__ == "__main__":
    while True:
        print(f"I am running! ({datetime.datetime.now()})")
        time.sleep(10)

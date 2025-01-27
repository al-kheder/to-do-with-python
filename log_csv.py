# log_csv.py

import csv
import os
import time

def log(message):
    file_exists = os.path.isfile('logs.csv')
    with open('logs.csv', mode='a') as file:
        fieldnames = ['Time', 'Message']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow({'Time': time.asctime(time.localtime(time.time())), 'Message': message})

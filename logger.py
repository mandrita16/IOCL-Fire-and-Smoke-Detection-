import csv
import os

def save_log(event, confidence, timestamp):

    file = "logs/fire_log.csv"

    exists = os.path.isfile(file)

    with open(file, "a", newline="") as f:

        writer = csv.writer(f)

        if not exists:
            writer.writerow(
                ["Time","Event","Confidence"]
            )

        writer.writerow(
            [timestamp,event,confidence]
        )
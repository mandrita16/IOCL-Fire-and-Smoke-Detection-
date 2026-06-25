from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

LOG_FILE = "logs/fire_log.csv"

@app.get("/")
def home():

    return {
        "status":"running"
    }

@app.get("/latest")

def latest():

    if not os.path.exists(LOG_FILE):

        return {
            "message":"No events"
        }

    df = pd.read_csv(LOG_FILE)

    if len(df) == 0:

        return {
            "message":"No events"
        }

    return df.tail(1).to_dict(
        orient="records"
    )[0]

@app.get("/all")

def all_logs():

    if not os.path.exists(LOG_FILE):

        return []

    df = pd.read_csv(LOG_FILE)

    return df.to_dict(
        orient="records"
    )
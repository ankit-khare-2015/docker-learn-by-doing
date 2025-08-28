from fastapi import FastAPI
from pathlib import Path
import os
from datetime import datetime

app = FastAPI()

DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = DATA_DIR / "visits.log"

@app.get("/")
def root():
    msg = os.getenv("APP_MESSAGE", "Hello from Docker ")
    # log a visit to demonstrate volumes/persistence
    with LOG_FILE.open("a") as f:
        f.write(f"{datetime.utcnow().isoformat()}Z - visited\n")
    return {"message": msg, "note": "Check /app/data/visits.log inside the container or the mounted folder."}

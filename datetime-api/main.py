from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/datetime")
def get_datetime():
    return {"datetime": datetime.utcnow().isoformat() + "Z"}


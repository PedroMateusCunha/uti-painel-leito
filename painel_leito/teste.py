import requests

from fastapi import FastAPI

app = FastAPI()
 
@app.get("/")
async def read_root():
    response = requests.get("http://10.0.0.254:7002/status")
    return {"status": response.status_code, "response": response.json()}
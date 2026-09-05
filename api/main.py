from fastapi import FastAPI
from lib.genus import genus

app = FastAPI(title="My API", version="1.0.0")

@app.get('/welcome')
def welcome():
    return {"msg": "Welcome to Genus APIs!"}
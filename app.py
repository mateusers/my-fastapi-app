from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Multiplier API", version="1.0")

class NumberInput(BaseModel):
    number: float

@app.get("/")
def read_root():
    return {"message": "Welcome! use - POST /multiply"}

@app.post("/multiply")
def multiply_number(request: NumberInput):
    result = request.number * 10
    return {
        "input": request.number,
        "result": result,
        "operation": "number * 10"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
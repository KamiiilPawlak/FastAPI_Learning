from fastapi import FastAPI, Query
import numpy as np
from datetime import datetime


def log_operation(operation: str, num1: float, num2: float):
    with open("log.txt", "a") as log:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log.write(f"{timestamp} | {operation} | {num1} | {num2}\n")

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "this is a calculator :DD"}

@app.get("/add")
async def add(num1: float, num2: float):
    try:
        result = num1 + num2
        log_operation("add", num1, num2)
        return {"Operation":"add","result":result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/subtract")
async def subtract(num1: float, num2: float):

    try:
        result = num1 - num2
        log_operation("subtract", num1, num2)
        return {"Operation": "subtract", "result": result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/multiply")
async def multiply(num1: float, num2: float):
    try:
        result = num1 * num2
        log_operation("multiply", num1, num2)
        return {"Operation": "multiply", "result": result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/divide")
async def divide(num1: float, num2: float):
    try:
        if num2 == 0:
            raise ValueError("divide by zero")
        result = num1 / num2
        log_operation("divide", num1, num2)
        return {"Operation": "multiply", "result": result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/trigonometric_function/sin")
async def sin(num1: float = Query(..., description="Wartość w radianach, dowolna liczba")):
    try:
        result = np.sin(num1)
        log_operation("sin", num1)
        return {"operation": "sin", "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/cos")
async def cos(num1: float):
    try:
        result = np.cos(num1)
        log_operation("cos", num1)
        return {"operation": "cos", "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/tan")
async def tan(num1: float):
    try:
        result = np.tan(num1)
        log_operation("tan", num1)
        return {"operation": "tan", "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/asin")
async def asin(num1: float):
    try:
        result = np.arcsin(num1)
        log_operation("asin", num1)
        return {"operation": "asin", "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/atan")
async def atan(num1: float):
    try:
        result = np.arctan(num1)
        log_operation("atan", num1)
        return {"operation": "atan", "result": result}
    except Exception as e:
        return {"error": str(e)}
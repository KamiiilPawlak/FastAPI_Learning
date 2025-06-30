from fastapi import FastAPI, Query
import numpy as np


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "this is a calculator :DD"}

@app.get("/add")
async def add(num1: float, num2: float):
    try:
        result = num1 + num2
        return {"Operation":"add","result":result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/subtract")
async def subtract(num1: float, num2: float):

    try:
        result = num1 - num2
        return {"Operation": "subtract", "result": result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/multiply")
async def multiply(num1: float, num2: float):
    try:
        result = num1 * num2
        return {"Operation": "multiply", "result": result}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/divide")
async def divide(num1: float, num2: float):
    try:
        if num2 == 0:
            raise ValueError("divide by zero")
        result = num1 / num2
        return {"Operation": "multiply", "result": result}
    except Exception as e:
        return {"Error": str(e)}
@app.get("/trigonometric_function/sin")
async def sin(num1: float = Query(..., description="Wartość w radianach, dowolna liczba")):
    try:
        return {"operation": "sin", "result": np.sin(num1)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/cos")
async def cos(num1: float):
    try:
        return {"operation": "cos", "result": np.cos(num1)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/tan")
async def tan(num1: float):
    try:
        return {"operation": "tan", "result": np.tan(num1)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/asin")
async def asin(num1: float):
    try:
        result = np.arcsin(num1)
        return {"operation": "asin", "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/trigonometric_function/atan")
async def atan(num1: float):
    try:
        return {"operation": "atan", "result": np.arctan(num1)}
    except Exception as e:
        return {"error": str(e)}
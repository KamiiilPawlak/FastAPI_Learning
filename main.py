from fastapi import FastAPI
import numpy as np


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "this is a calculator :DD"}

@app.get("/add")
async def add(num1: float, num2: float):
    return num1 + num2

@app.get("/subtract")
async def subtract(num1: float, num2: float):
    return num1 - num2

@app.get("/multiply")
async def multiply(num1: float, num2: float):
    return num1 * num2

@app.get("/divide")
async def divide(num1: float, num2: float):
    return num1 / num2

@app.get("/trigonometric_function/sin")
async def sin(num1: float):
    return np.sin(num1)

@app.get("/trigonometric_function/cos")
async def cos(num1: float):
    return np.cos(num1)

@app.get("/trigonometric_function/tan")
async def tan(num1: float):
    return np.tan(num1)

@app.get("/trigonometric_function/asin")
async def asin(num1: float):
    return np.arcsin(num1)


@app.get("/trigonometric_function/atan")
async def atan(num1: float):
    return np.arctan(num1)



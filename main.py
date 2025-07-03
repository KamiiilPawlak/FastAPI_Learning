from fastapi import FastAPI, Query
import numpy as np
from datetime import datetime
from typing import List, Union
from enum import Enum



def log_operation(operation: str, num1: float, num2: float = None):
    with open("log.txt", "a") as log:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if num2 is not None:
            log.write(f"{timestamp} | {operation} | {num1} | {num2}\n")
        else:
            log.write(f"{timestamp} | {operation} | {num1}\n")






class ModelName(str, Enum):
    alexnet = "AlexNet"
    resnet = "ResNet"
    lennet = "Lenet"



class MathConst(float, Enum):
    PI = 3.1415926
    e = 2.71828




app = FastAPI()


#czyli w przypadku zadeklarowania innych parametrow funkji. ktore nie sa czescia sciezki, sa one autoamtycznei interpetowane jako parametry zapytania
fake_items_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items/")
async def read_items(skip: int =0, limit: int =10):
    return fake_items_db[skip : skip + limit]




@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning model"}
    if model_name.value == "Lenet":
        return {"model_name": ModelName.lennet, "message": "Lenet model"}




@app.get("/List")
async def new_list(lista: List[Union[str, int]] = Query(default=None)):
    #asynchronicznie
    if lista is None:
        lista = []
    return {"received_list": lista}


@app.get("/name/{name2}")  #decorator
async def root(name2: str):
    return {"message": name2}




@app.get("/extra")

# nie asynchronicznie
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name




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
            raise ValueError("Nie można dzielić przez zero")
        result = num1 / num2
        log_operation("divide", num1, num2)
        return {"Operation": "divide", "result": result} # Poprawiona literówka
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
        if not -1 <= num1 <= 1:
            raise ValueError("Wartość dla asin musi być w zakresie [-1, 1]")
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
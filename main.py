from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict


app = FastAPI()

#model of users
class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, title="Name", description="Name of user")
    age: int = Field(..., ge=18, title="Age", description="Age of user")
    email: EmailStr = Field(..., title="Email", description="Email of user")
    phone: Optional[str] = None


#simulator DB
simulatorDB: Dict[int, User] = {}
id_counter = 1


#CRUD


#CREATE - add users
@app.post("/users/")
def create_user(user: User):
    global id_counter
    simulatorDB[id_counter] = user
    response = {"id": id_counter, "name":user}
    id_counter+=1
    return response



#READ users
@app.get("/users/")
def read_users():
    return simulatorDB



@app.get("/users/{user_id}")
def read_user(user_id: int = Path(..., gt=0)):
    if user_id not in simulatorDB:
        raise HTTPException(status_code=404, detail="User not found")
    return simulatorDB[user_id]


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in simulatorDB:
        raise HTTPException(status_code=404, detail="User not found")
    simulatorDB[user_id] = user
    return {"message":"Uzytkownik zaktualizowany", "id": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in simulatorDB:
        raise HTTPException(status_code=404, detail="User not found")
    del simulatorDB[user_id]
    return{"message":f"Uztkownik {user_id} zostal usuniety"}
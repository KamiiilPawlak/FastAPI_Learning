from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict


app = FastAPI()

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, title="Name", description="Name of user")
    age: int = Field(..., ge=18, gt = 100, title="Age", description="Age of user")
    email: EmailStr = Field(..., title="Email", description="Email of user")
    phone: Optional[str] = None



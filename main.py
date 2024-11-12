from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os
import json

app = FastAPI()

DATA_FOLDER = "/home/juanda/FinalSistemasOperativosJuanOliveros/user_data"

os.makedirs(DATA_FOLDER, exist_ok=True)

class User(BaseModel):
    name: str
    age: int
    profession: str

@app.post("/user")
async def create_user(user: User):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"user_{timestamp}.json"

    file_path = os.path.join(DATA_FOLDER, file_name)

    with open(file_path, "w") as f:
        json.dump(user.dict(), f, indent=4)

    return {"nombre": user.name, "edad": user.age, "profesion": user.profession}
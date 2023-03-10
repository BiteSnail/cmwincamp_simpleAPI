from fastapi import FastAPI, Body
from src.data.user import User
from src.data.mydb import Mydb
from starlette.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()
db = Mydb()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/birth",)
async def get_birth(user:User = Body()):
    user.birthday = db.find_one_select(user.username)
    return user

@app.get("/names")
async def get_names():
    return {"names":db.get_items()}
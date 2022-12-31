from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    _id: int
    username: str
    birthday: datetime
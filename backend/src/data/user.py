from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    _id: int | None
    username: str
    birthday: datetime | None
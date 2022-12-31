# API Architecture
## REST API

> **get_birth(name)**   
>
> POST   
> http://localhost.com/app/api/getBirth   
> *Return OK(200)*, Birth data

## Data Structure
```Python
from pydantic import BaseModel
from datatime import datetime

class User(BaseModel):
    _id: int
    username: str
    birth: datetime
```
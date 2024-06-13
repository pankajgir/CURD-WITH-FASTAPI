from pydantic import BaseModel


class user(BaseModel):
    name:str
    email:str
    phone:str
    password:str

class show(BaseModel):
    id:int
class showname(BaseModel):
    name:str

class update(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    password:str
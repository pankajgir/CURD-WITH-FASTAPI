from fastapi import APIRouter
from . models import *
from . pydentic_models import user, show,showname,update
from passlib.context import CryptContext

app=APIRouter()
pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


def get_password(password):
    return pwd_context.hash(password)


@app.post("/")
async def create_user(data:user):
    if await  Personone.exists(email=data.email):
        return {"status":False, "massage":"email alrady exixts"}

    elif await Personone.exists(phone=data.phone):
        return {"status":False, "massage":"phone alrady exixts"}
    
    else:
        user_obj= await Personone.create(name=data.name,
                                         email=data.email,
                                         phone=data.phone,
                                         password= get_password(data.password))
        return user_obj

@app.get("/show_data/")
async def show_user():
    user_obj = await Personone.all()
    return user_obj

@app.post("/show_id_vise/")
async def id(data:show):
    user_obj = await Personone.get(id=data.id)
    return user_obj

@app.post("/filter_name/")
async def show_name(data:showname):
    user_obj = await Personone.filter(name=data.name)
    return user_obj

@app.delete('/delete_user/')
async def delete_user(data:show):
    user_obj = await Personone.get(id=data.id).delete()
    return user_obj

@app.put('/update/')
async def update_user(data:update):
     user_obj = await Personone.get(id=data.id)
     obj = await Personone.filter(id=data.id).update(name=data.name,email=data.email,
                                                     phone=data.phone)

     return obj


     


     
     

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI() 

"""class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
def user_details(user: User):
    return {"message":"user details created","data":user} """

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
   name:str
   age:int
   address:Address

@app.post("/createusers")
def createuser(user:User):
    return {
        "message": "User created successfully",
        "user": user
    }






         
    

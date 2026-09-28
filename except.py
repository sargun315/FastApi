from fastapi import FastAPI, status, HTTPException

app = FastAPI()
class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="usrer nahi hai found"
        )
    return{
        "id": 1,
        "name": "sargun kumar", 
        "age": 22
    }

@app.get("/user/{name}")
def get_user(name: str):
    if name != "sargun":
        raise UserNotFoundException(name)
    return{
        "name":name 
    }
from fastapi import FastAPI, status,HTTPException

app = FastAPI()

@app.post("/user",status_code=status.HTTP_201_CREATED)
def user():
    return {"message": "User created successfully"}


@app.get("/user")
def get_user():
    return{
        "status":"successful",
        "message":"User fetched successfully",
        "data":"sargun kumar",
        "age":22
    }


@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return{
         "id":1,
         "name":"sargun kumar",
         "age":22
    }

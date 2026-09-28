from fastapi import FastAPI
app = FastAPI()
@app.post("/users")
def create_user(users: dict):
    return {"message":"users details","data":users}
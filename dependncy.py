from fastapi import FastAPI, Depends

app = FastAPI()


# Dependency function
def common_parameters():
    return {
        "name": "Sargun",
        "course": "FastAPI"
    }


# API route
@app.get("/users")
def get_users(data=Depends(common_parameters)):
    return {
        "message": "User data",
        "data": data
    }
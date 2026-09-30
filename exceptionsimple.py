from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="User ID must be greater than 0"
        )

    return {
        "user_id": user_id,
        "message": "User found"
    }
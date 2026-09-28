from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "sargun kumar"}

@app.get("/about")
def about():
    return {"name": "Sargun", "course": "Python FastAPI"}

@app.get("/users")
def users():
    return {
        "users": [
            {"name": "Sargun", "course": "Python FastAPI"},
            {"name": "Rahul", "course": "Python"},
            {"name": "Aman", "course": "FastAPI"}
        ]
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def name():
    return {"message": "sargun kumar"}

@app.get("/about")
def about():
    return {"name": "Sargun", "course": "Python FastAPI"}   

@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

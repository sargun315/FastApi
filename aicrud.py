
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student CRUD API")
git
# -----------------------
# Pydantic Model
# -----------------------
class Student(BaseModel):
    name: str
    age: int
    course: str

# Fake Database
students = []
student_id = 1

# -----------------------
# Home API
# -----------------------
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD API"}

# -----------------------
# CREATE
# -----------------------
@app.post("/students")
def create_student(student: Student):
    global student_id

    new_student = {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)
    student_id += 1

    return {
        "message": "Student Added Successfully",
        "data": new_student
    }

# -----------------------
# READ ALL
# -----------------------
@app.get("/students")
def get_students():
    return students

# -----------------------
# READ ONE
# -----------------------
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(status_code=404, detail="Student Not Found")

# -----------------------
# UPDATE
# -----------------------
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):

    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return {
                "message": "Student Updated Successfully",
                "data": student
            }

    raise HTTPException(status_code=404, detail="Student Not Found")

# -----------------------
# DELETE
# -----------------------
@app.delete("/students/{id}")
def delete_student(id: int):

    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message": "Student Deleted Successfully"}

    raise HTTPException(status_code=404, detail="Student Not Found")
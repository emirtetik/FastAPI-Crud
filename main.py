from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

students = {
    1: {
        "name": "jhon",
        "age": 14,
        "class": "year 12"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"} 

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):  
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student_by_name(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "not found"}

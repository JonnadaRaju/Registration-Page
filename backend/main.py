from fastapi import FastAPI
from database import create_students_table, get_db_connection
from models import Student

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting up the application...") 
    create_students_table()
    

@app.get("/")
async def root():
    return {"message": "Welcome to the Student Registration API!"}   
    
@app.post("/register")
async def register_student(student: Student):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, phone, course) VALUES (?, ?, ?, ?)", (student.name, student.email, student.phone, student.course))
    conn.commit()
    conn.close()
    return {"message": "Student registered successfully"}


@app.get("/students")
async def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return {"students": [dict(student) for student in students]}
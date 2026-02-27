from fastapi import FastAPI, Depends
from database import create_students_table, get_db_connection, get_db
from models import Student
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    print("Starting up the application...") 
    create_students_table()
    

@app.get("/")
async def root():
    return {"message": "Welcome to the Student Registration API!"}   
    
@app.post("/register")
async def register_student(student: Student, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, email, phone, course) VALUES (?, ?, ?, ?)", (student.name, student.email, student.phone, student.course))
    db.commit()
    return {"message": "Student registered successfully"}


@app.get("/students")
async def get_students(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return {"students": [dict(student) for student in students]}
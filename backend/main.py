from fastapi import FastAPI
from database import create_students_table

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting up the application...") 
    create_students_table()
from fastapi import FastAPI


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting up the application...") 
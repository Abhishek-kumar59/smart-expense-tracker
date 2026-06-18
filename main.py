from fastapi import FastAPI

from app.api.test_db import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Smart Expense Tracker API"}
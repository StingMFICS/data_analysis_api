from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Data Analysis API")

# Подключение маршрутов
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to the Data Analysis API!"}

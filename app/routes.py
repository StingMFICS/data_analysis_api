from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.utils import analyze_data

router = APIRouter()


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Загружает файл и анализирует данные.
    Поддерживаются форматы: CSV, JSON.
    """
    if file.content_type not in ["text/csv", "application/json"]:
        raise HTTPException(status_code=400, detail="Please upload CSV or JSON.")

    try:
        # Чтение данных
        if file.content_type == "text/csv":
            data = pd.read_csv(file.file)
        else:
            data = pd.read_json(file.file)

        # Анализ данных
        result = analyze_data(data)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

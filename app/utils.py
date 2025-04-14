def analyze_data(data):
    """
    Выполняет базовый анализ данных и возвращает статистику.
    """
    analysis = {
        "columns": list(data.columns),
        "rows": len(data),
        "mean": data.mean(numeric_only=True).to_dict(),
        "median": data.median(numeric_only=True).to_dict(),
        "null_values": data.isnull().sum().to_dict(),
    }
    return analysis

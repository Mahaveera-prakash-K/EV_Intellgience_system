import os
from .config import DATA_FOLDER
def save_dataset(df, file_format):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    if file_format == "csv":
        path = f"{DATA_FOLDER}/ev_dataset.csv"
        df.to_csv(path, index=False)
    elif file_format == "json":
        path = f"{DATA_FOLDER}/ev_dataset.json"
        df.to_json(path, orient="records")
    elif file_format == "xlsx":
        path = f"{DATA_FOLDER}/ev_dataset.xlsx"
        df.to_excel(path, index=False)
    print(f"\nDataset saved successfully → {path}")
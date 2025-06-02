import os
import shutil
from typing import List

UPLOAD_DIR = "uploaded_files"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Store filenames and paths here for simplicity
uploaded_files = {}

def save_files(files: List) -> List[str]:
    saved = []
    for file in files:
        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        uploaded_files[file.filename] = path
        saved.append(file.filename)
    return saved

def list_files() -> List[str]:
    return list(uploaded_files.keys())

def delete_file(filename: str):
    if filename not in uploaded_files:
        raise FileNotFoundError(f"File {filename} not found")
    os.remove(uploaded_files[filename])
    del uploaded_files[filename]

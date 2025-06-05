import os
import shutil
from typing import List
from app.core.file_utils import extract_text_from_file
from app.core.vector_store import add_document_chunks

UPLOAD_DIR = "uploaded_files"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Store filenames and paths here for simplicity
uploaded_files = {}

def split_into_chunks(text: str, max_words: int = 200) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


# def save_files(files: List) -> List[str]:
#     saved = []
#     for file in files:
#         path = os.path.join(UPLOAD_DIR, file.filename)
#         with open(path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#         uploaded_files[file.filename] = path
#         saved.append(file.filename)
#     return saved

def save_files(files: List) -> List[str]:
    saved = []
    for file in files:
        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        uploaded_files[file.filename] = path
        saved.append(file.filename)

        # Process for vector search
        text = extract_text_from_file(path)
        chunks = split_into_chunks(text)
        add_document_chunks(chunks)
    return saved

def list_files() -> List[str]:
    return list(uploaded_files.keys())

def delete_file(filename: str):
    if filename not in uploaded_files:
        raise FileNotFoundError(f"File {filename} not found")
    os.remove(uploaded_files[filename])
    del uploaded_files[filename]

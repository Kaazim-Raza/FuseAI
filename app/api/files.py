from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from app.storage.file_storage import save_files, list_files, delete_file

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    saved_files = save_files(files)
    return {"uploaded_files": saved_files}

@router.get("/")
async def get_files():
    return {"files": list_files()}

@router.delete("/{filename}")
async def remove_file(filename: str):
    try:
        delete_file(filename)
        return {"detail": f"File '{filename}' deleted"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

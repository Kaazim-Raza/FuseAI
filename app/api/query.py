from fastapi import APIRouter, Query, HTTPException
from app.storage.file_storage import uploaded_files
from app.core.file_utils import extract_text_from_file
from app.core.gemini import query_gemini_api

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/")
async def ask_question(query: str = Query(...)):
    if not uploaded_files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    # Combine all files' text as context
    context = ""
    for file_path in uploaded_files.values():
        text = extract_text_from_file(file_path)
        context += text + "\n---\n"

    response = await query_gemini_api(query, context)
    return {"query": query, "response": response}

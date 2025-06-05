from fastapi import APIRouter, Query, HTTPException
from app.storage.file_storage import uploaded_files
from app.core.file_utils import extract_text_from_file
from app.core.gemini import query_gemini_api
from app.core.vector_store import search_similar_chunks

router = APIRouter(prefix="/query", tags=["query"])

# @router.post("/")
# async def ask_question(query: str = Query(...)):
#     if not uploaded_files:
#         raise HTTPException(status_code=400, detail="No files uploaded")

#     # Combine all files' text as context
#     context = ""
#     for file_path in uploaded_files.values():
#         text = extract_text_from_file(file_path)
#         context += text + "\n---\n"

#     response = await query_gemini_api(query, context)
#     return {"query": query, "response": response}



@router.post("/")
async def ask_question(query: str = Query(...)):
    if not uploaded_files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    # Search vector DB for relevant chunks
    relevant_chunks = search_similar_chunks(query)

    if not relevant_chunks:
        return {"query": query, "response": "No relevant information found in uploaded documents."}

    context = "\n---\n".join(relevant_chunks)
    response = await query_gemini_api(query, context)
    return {"query": query, "response": response}
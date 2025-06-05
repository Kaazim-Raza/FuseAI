import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Small and fast

# Index and associated chunk metadata
index = faiss.IndexFlatL2(384)  # 384 is dimension of MiniLM
chunk_texts = []

def add_document_chunks(chunks: list[str]):
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings).astype('float32'))
    chunk_texts.extend(chunks)
    print("chunks",embeddings)

def search_similar_chunks(query: str, top_k: int = 5, threshold: float = 0.6) -> list[str]:
    query_vec = model.encode([query]).astype('float32')
    D, I = index.search(query_vec, top_k)
    print("query_vec", query_vec)

    results = []
    for dist, idx in zip(D[0], I[0]):
        if dist <= threshold and idx < len(chunk_texts):
            results.append(chunk_texts[idx])
    return results

import os
import PyPDF2
import pandas as pd

def extract_text_from_file(file_path: str) -> str:
    ext = file_path.split('.')[-1].lower()
    if ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == "pdf":
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            return "\n".join(text)
    elif ext in ("xls", "xlsx"):
        df = pd.read_excel(file_path)
        return df.to_string()
    else:
        return ""

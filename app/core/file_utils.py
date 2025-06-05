# import os
# import PyPDF2
# import pandas as pd

# def extract_text_from_file(file_path: str) -> str:
#     ext = file_path.split('.')[-1].lower()
#     if ext == "txt":
#         with open(file_path, "r", encoding="utf-8") as f:
#             return f.read()
#     elif ext == "pdf":
#         with open(file_path, "rb") as f:
#             reader = PyPDF2.PdfReader(f)
#             text = []
#             for page in reader.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text.append(page_text)
#             # print(f"Extracted {text} pages from PDF.")
#             print("\n\n".join(text))
#             return "\n\n".join(text)
#     elif ext in ("xls", "xlsx"):
#         df = pd.read_excel(file_path)
#         return df.to_string()
#     else:
#         return ""


import PyPDF2
import pandas as pd
import re

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
                    # 🧹 Clean up line breaks and extra spaces
                    cleaned = re.sub(r'\s+', ' ', page_text).strip()
                    text.append(cleaned)
            combined = "\n\n".join(text)
            print(combined)  # Optional for debug
            return combined

    elif ext in ("xls", "xlsx"):
        df = pd.read_excel(file_path)
        return df.to_string()

    else:
        return ""

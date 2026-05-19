import os
import uuid
from fastapi import UploadFile

def ensure_directories():
    os.makedirs("static/uploads", exist_ok=True)
    os.makedirs("static/results", exist_ok=True)

def get_static_dir():
    return "static"

def get_file_url(filename, subdir):
    return f"/{subdir}/{filename}"

async def save_upload_file(file: UploadFile, upload_dir: str) -> str:
    ext = os.path.splitext(file.filename)[1] if file.filename else ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return filename

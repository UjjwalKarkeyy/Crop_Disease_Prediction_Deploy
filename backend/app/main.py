from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
# async to run this in parallel with others
async def create_file(file: Annotated[bytes, File()]): # tells fast api type hint and where it comes from
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename} 

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from PIL import Image
import io
import uvicorn
import joblib
import numpy as np
import utils # run utils.py before running main.py

pipeline = joblib.load("./crop_disease_pipeline.pkl")

app = FastAPI()
origins = [
    'http://croplysis.karkiujjwal.com.np',
    'https://croplysis.karkiujjwal.com.np',
]
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.post('/predict')
async def predict(file: Annotated[UploadFile, File()]):
    # read file bytes
    contents = await file.read()
    results = []
    # convert bytes -> PIL Image (for processing)
    image = Image.open(io.BytesIO(contents))
    labels = [
    'Pepper Bell Bacterial Spot',
    'Pepper Bell Healthy',
    'Potato Early Blight',
    'Potato Healthy',
    'Potato Late Blight',
    'Tomato Target Spot',
    'Tomato Mosaic Virus',
    'Tomato Yellow Leaf Curl Virus',
    'Tomato Bacterial Spot',
    'Tomato Early Blight',
    'Tomato Healthy',
    'Tomato Late Blight',
    'Tomato Leaf Mold',
    'Tomato Septoria Leaf Spot',
    'Tomato Spider Mites',
    ]  
    pred = pipeline.predict([image])
    top3_idx = np.argsort(pred[0])[::-1][:3] # descend and take top 3
    results = [
        {"label": labels[i], "confidence": round(float(pred[0][i]), 2)}
        for i in top3_idx
    ]

    return {"predictions": results}
 

if __name__ == "__main__":
    # "main:app", find main.py then app
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
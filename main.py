import os

from typing import Any
from fastapi import FastAPI, File, UploadFile
from detect_from_video import detection
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

origins = [
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/detection/")
async def deepfakes_detection():
    return detection(r"C:\Users\User\Downloads\Video\obama_deepfake.mp4", r'C:\Users\User\Downloads\Compressed\models\full\xception\full_c40.p', r'C:\Users\User\Downloads\Video')

@app.post("/upload")
async def upload_videos(file: UploadFile = File(...)):
    try:
        os.mkdir("videos")
        print(os.getcwd())
    except Exception as e:
        print(e) 
    file_name = os.getcwd()+"/videos/"+file.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(file.file.read())
        f.close()

    filePath = jsonable_encoder({"filePath": file_name})
    return detection(file_name, r'C:\Users\User\Downloads\Compressed\models\full\xception\full_c40.p', r'C:\Users\User\Documents\obsidian\result')
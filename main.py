from fastapi import FastAPI
from detect_from_video import detection

app = FastAPI()

@app.get("/detection/")
async def deepfakes_detection():
    return detection(r"C:\Users\User\Downloads\Video\obama_deepfake.mp4", r'C:\Users\User\Downloads\Compressed\models\full\xception\full_c40.p', r'C:\Users\User\Downloads\Video')
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/get-url")
def get_video_url(youtube_url: str):
    try:
        cmd = ["yt-dlp", "-g", "-f", "best[ext=mp4]/best", youtube_url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        direct_url = result.stdout.strip().split("\n")[0]
        return {"download_url": direct_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

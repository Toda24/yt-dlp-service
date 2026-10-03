from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/get-url")
def get_video_url(youtube_url: str):
    try:
        # Use format 18 or 'best[height<=720][ext=mp4]' which doesn't require ffmpeg merging
        cmd = ["yt-dlp", "-g", "-f", "18/mp4", youtube_url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        direct_url = result.stdout.strip().split("\n")[0]
        return {"download_url": direct_url}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"yt-dlp error: {e.stderr.strip() or e.stdout.strip()}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

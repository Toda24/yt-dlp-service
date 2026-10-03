from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/get-url")
def get_video_url(youtube_url: str):
    try:
        # Use the android player client to bypass JS runtime requirements and web bot blocks
        cmd = [
            "yt-dlp",
            "--extractor-args", "youtube:player_client=android",
            "-g",
            "-f", "18/mp4",
            youtube_url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        direct_url = result.stdout.strip().split("\n")[0]
        return {"download_url": direct_url}
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() or e.stdout.strip()
        raise HTTPException(status_code=500, detail=f"yt-dlp error: {error_msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

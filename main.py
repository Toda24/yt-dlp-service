from fastapi import FastAPI, HTTPException
import os
import yt_dlp

app = FastAPI()

@app.get("/get-url")
def get_download_url(youtube_url: str):
    # Get the absolute path of the directory where main.py lives
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cookie_path = os.path.join(BASE_DIR, "cookies.txt")

    ydl_opts = {
        'format': '18/mp4',
        'geturl': True,
        'cookiefile': cookie_path,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            direct_url = ydl.extract_info(youtube_url, download=False)
            if isinstance(direct_url, dict):
                direct_url = direct_url.get('url')
        return {"download_url": direct_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

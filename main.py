from fastapi import FastAPI, HTTPException
import yt_dlp

app = FastAPI()

@app.get("/get-url")
def get_download_url(youtube_url: str):
    ydl_opts = {
        'format': '18/mp4',
        'geturl': True,
        'cookiefile': 'cookies.txt',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract direct URL safely using internal Python bindings
            direct_url = ydl.extract_info(youtube_url, download=False)
            if isinstance(direct_url, dict):
                direct_url = direct_url.get('url')
        return {"download_url": direct_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

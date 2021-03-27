from pydantic import BaseModel

class AudioDownloadRequest(BaseModel):
    url: str
    artist: str
    album: str
    title: str

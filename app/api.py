from sys import path
from download_logger import DownloadLogger
from fastapi import APIRouter, Response
import youtube_dl
import mutagen
import os
import uuid
import shutil
import logging

from models import AudioDownloadRequest

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

library_dir = ''

def progress_hook(d):
    if d['status'] == 'finished':
        file_name = d['filename']
        logger.info('Done downloading: {}, now converting...'.format(file_name))

@router.post('/api', status_code=200)
async def download_video(request: AudioDownloadRequest, response: Response):

    logger.info("Downloading audio from video url: {}".format(request.url))

    global library_dir
    logger.info("Using Music Library directory: {}".format(library_dir))

    temp_id = str(uuid.uuid4())

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'vorbis',
           'preferredquality': '9'
         }],
         'logger': DownloadLogger(),
         'progress_hooks': [progress_hook],
         'addmetadata': True,
         'quiet': False,
         'forcefilename': True,
         'outtmpl': 'temp_audio/{}.temp'.format(temp_id)
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.url])

    audio = mutagen.File('temp_audio/{}.ogg'.format(temp_id), easy=True)
    audio["TITLE"] = request.title
    audio["ARTIST"] = request.artist
    audio["ALBUM"] = request.album
    audio.save()

    path = '{0}/{1}/{2}/'.format(library_dir, request.artist, request.album)
    if not os.path.exists(path):
        os.makedirs(path)

    shutil.move('temp_audio/{}.ogg'.format(temp_id), '{0}/{1}/{2}/{1} - {3}.ogg'.format(library_dir, request.artist, request.album, request.title))

    return {'message': 'Audio downloaded and extracted.'}

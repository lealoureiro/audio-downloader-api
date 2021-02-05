from sys import path
from flask import Blueprint
from flask import request
from flask import make_response, jsonify
from download_logger import DownloadLogger
import youtube_dl
import mutagen
import os
import uuid
import shutil

download_video_api = Blueprint('api', __name__)
library_dir = ''

def progress_hook(d):
    if d['status'] == 'finished':
        file_name = d['filename']
        print('Done downloading: {}, now converting...'.format(file_name))

@download_video_api.route('/api', methods=['POST'])
def download_video():

    global library_dir

    content = request.get_json()

    if 'url' not in content:
        return bad_request('URL not provided.')

    url = content['url']

    if 'artist' not in content:
        return bad_request('Artist not provided.')

    artist = content['artist']

    if 'album' not in content:
        return bad_request('Album not provided.')    

    album = content['album']

    if 'title' not in content:
        return bad_request('Song title not provided.')    

    title = content['title']

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
        ydl.download([url])

    audio = mutagen.File('temp_audio/{}.ogg'.format(temp_id), easy=True)
    audio["TITLE"] = title
    audio["ARTIST"] = artist
    audio["ALBUM"] = album
    audio.save()

    path = '{0}/{1}/{2}/'.format(library_dir, artist, album)
    if not os.path.exists(path):
        os.makedirs(path)

    shutil.move('temp_audio/{}.ogg'.format(temp_id), '{0}/{1}/{2}/{1} - {3}.ogg'.format(library_dir, artist, album, title))

    message = {'status': 'OK', 'message': 'Audio downloaded and extracted.'}
    return make_response(jsonify(message), 200)


def bad_request(message):
    message = {'errorMessage': message}
    return make_response(jsonify(message), 400)

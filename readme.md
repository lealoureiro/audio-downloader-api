# AudioDownloaderAPI

### REST API to download audio stream from content available in well know streaming services like Youtube, Soundcloud etc.

<br />

This is just a simple API where you can submit an API request with URL from a well know streaming service alongside some data regarding the author and music stream from the video will be saved as file in location of your preference.

<br/> 

### Example request:

`URI: POST /api`
```json
{
    "url": "https://www.youtube.com/watch?v=LyCEN_zTE54",
    "artist": "Purple Disco Machine",
    "album": "Sets",
    "title": "Special Mix 2021. Bests Songs & Remixes"
}
```

The application will download the audio stream of the video avaible in the url **https://www.youtube.com/watch?v=LyCEN_zTE54**. 

The output will be an audio file encoded in **Ogg Vorbis** with maximum quality available using the [FFmpeg](https://www.ffmpeg.org/) utility.

The result file will be located in the specified Library Directory in the following format:

`<LibraryDir>/<Artist>/<Album>/<Artist> - <Title>.ogg`

In the case of the previous request:
`<LibraryDir>/Purple Disco Machine/Sets/Purple Disco Machine - Special Mix 2021. Bests Songs & Remixes.ogg`

<br/>

The streaming services supported are the ones that are supported by the python application [youtube-dl](https://github.com/ytdl-org/youtube-dl/).

## Pre-requisites
- Python 3.6+
- Pip
- FFmpeg

<br/>

## Running the application in shell:
```bash
git clone https://github.com/lealoureiro/mortgage-calculator-api.git
cd app
pip3 install -r requirements.txt
LIBRARY_DIR=<YourMusicFolder> python3 main.py
```
Please replace **\<YourMusicFolder\>** with your actual music Library folder or wherever you want to save the output music files.

## Running inside docker container:
```bash
docker run --rm --name audio-downloader -p 80:80 -v <YourMusicFolder>:/music lealoureiro/audio-downloader-api
```
Please replace **\<YourMusicFolder\>** with your actual music Library folder or wherever you want to save the output music files.
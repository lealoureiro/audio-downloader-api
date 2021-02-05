
from flask import Flask
from api import download_video_api
import os
import api


def create_app():

    api.library_dir = os.getenv("LIBRARY_DIR", '.')

    app = Flask(__name__)
    app.register_blueprint(download_video_api)

    return app

if __name__ == "__main__":
    create_app().run()

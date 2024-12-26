from flask import Flask, jsonify, send_file, Blueprint, request,abort
from flask_cors import CORS
import os
import lyrics

LYRICS_PATH = "/temp_lyric_files"
app = Flask(__name__)
CORS(app)



@app.route("/request-lyrics/<song_details>")
def request_lyrics(song_details):
    lyrics_text = lyrics.get_timed_lyrics(song_details)
    return lyrics_text


if __name__ == "__main__":
    app.run(debug=True, port=7070)


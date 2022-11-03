try:
    # from pytube import YouTube
    # from pytube import Playlist
    # import mysql.connector
    from flask import Flask, jsonify, request, Response
    # from mysql.connector import Error
    from time import sleep
    import re
    # import json
    # import database
    from source import youtube
except Exception as e:
    print("Some Modules are missing {}".format(e))

app = Flask(__name__)

# SITE_NAME = "137.26.8.213"

# @app.route('/')
# def index():
#     return "Flask is running!"

@app.route('/api')
def get_n2aa_replay():
    url = request.args.get('url', default='*', type=str)
    # sleep(2)
    print("Requesting data for ", url, "........")
    youtube.youtube_downloader(url)
    # res = jsonify(title=title)
    # (video_id, thumbnail, fn, path) = youtube.youtube_downloader(url)
    res = jsonify(yt_status="Done")
    # res = jsonify(video_id=video_id, thumb=thumbnail, filename=fn, path=path)
    # while res.headers.
    res.headers.add('Access-Control-Allow-Origin', '*')
    if Response(status="200") or Response(status="201"):
        # sleep(3)
        # print("\nTrying again for ", url, "........\n")
        # (title, fn, path) = youtube.youtube_downloader(url)
        # res = jsonify(title=title, filename=fn, path=path)
        # # while res.headers.
        # res.headers.add('Access-Control-Allow-Origin', '*')
        # return "OK", 200, res  # serialize and use JSON headers
        print("Request for ", url, " successful")
        return res  # serialize and use JSON headers
    else:
        print("Sorry, couldnt get request for ", url)

# @app.route('/<path:path>')
# def proxy(path):
#     # if request.method=='GET':
#         resp = requests.get(f'{SITE_NAME}{path}')
#         youtube.youtube_downloader(path)
#         # res = jsonify(title=title)
#         excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#         headers = [(name, value) for (name, value) in     resp.raw.headers.items() if name.lower() not in excluded_headers]
#         response = Response(resp.content, resp.status_code, headers)
#         return response


if __name__ == '__main__':
    app.run(
        debug=False,
        # port=80
        # threaded=True,
        host=app.config.get("HOST", "0.0.0.0"),
        port=app.config.get("PORT", 5000)
    )



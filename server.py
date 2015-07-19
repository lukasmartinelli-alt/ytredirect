import os
import pafy
from flask import Flask, redirect, request


app = Flask(__name__)
port = int(os.getenv("VCAP_APP_PORT", "5000"))


@app.route("/")
def download():
    url = request.args.get("url")

    if not url:
        return app.send_static_file('index.html')

    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    download_url = best.url_https
    return redirect(download_url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)

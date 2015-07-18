from flask import Flask, redirect, request
import pafy

app = Flask(__name__)

@app.route("/")
def download():
    url = request.args.get("url")
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    download_url = best.url_https
    return redirect(download_url)


if __name__ == "__main__":
    app.run()

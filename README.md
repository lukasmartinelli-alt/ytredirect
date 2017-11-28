# ytredirect ![stability-deprecated](https://img.shields.io/badge/stability-deprecated-red.svg)

> :warning: This repository is no longer maintained by Lukas Martinelli.

Redirect to the best [Youtube](https://youtube.com) direct media URL with the help of [pafy](https://github.com/mps-youtube/pafy).
~~Try it at http://ytredirect.lukasmartinelli.ch.~~

![Screenshot](screenshot.png)

## Use Cases

Download video with curl.

```
curl -Lo video.mp4 "ytredirect.lukasmartinelli.ch?url=http://www.youtube.com/watch?v=8TCxE0bWQeQ"
```

## Get started

Install requirements.

```
pip install -r requirements.txt
```

Run server and visit `localhost:5000`.

```
python server.py
```

Or use Docker.

```
docker run -p 5000:5000 lukasmartinelli/ytredirect
```

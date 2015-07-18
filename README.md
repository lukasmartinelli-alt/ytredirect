# ytredirect

Redirect to the best [Youtube](https://youtube.com) direct media URL with the help of [pafy](https://github.com/mps-youtube/pafy).
Try it at [http//ytredirect.tk](http//ytredirect.tk).

![Screenshot](screenshot.png)

## Use Cases

Download any video with curl.

```
curl -Lo video.mp4 "ytredirect.tk?url=http://www.youtube.com/watch?v=8TCxE0bWQeQ"
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

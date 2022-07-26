import functools

import requests
from flask import Blueprint, request, make_response
from PIL import Image
import pillow_avif
from io import BytesIO
from tenacity import retry, stop_after_attempt

from src.debug import clock

img_proxy = Blueprint("img_proxy", __name__)


def to_jpeg(img: bytes):
    result = Image.open(BytesIO(img)).convert('RGB')
    result_img = BytesIO()
    result.save(result_img, format="JPEG")
    return result_img.getvalue()


def to_jpeg_with_compress(img: bytes):
    result = Image.open(BytesIO(img)).convert('RGB')
    result = result.resize((int(result.size[0]/2), int(result.size[1]/2)), Image.ANTIALIAS)
    result_img = BytesIO()
    result.save(result_img, format="JPEG",optimize=True,quality=50)
    return result_img.getvalue()


@img_proxy.route("/image_proxy")
def img_proxy_handler():
    if request.args.get("compress") == "true":
        resp = make_response(get_image_content(request.args.get("url"), compress=True))
    else:
        resp = make_response(get_image_content(request.args.get("url"),  compress=False))
    resp.headers["Content-Type"] = "image/*"
    return resp


@functools.cache
def get_image_content(url, compress):
    if not compress:
        return to_jpeg(downloader(url))
    else:
        return to_jpeg_with_compress(downloader(url))


@retry(stop=stop_after_attempt(3))
def downloader(url, content_size=1024 * 128):
    headers = {"user-agent": 'Dart/2.10 (dart:io)'}
    # res = requests.get(url, stream=True, headers=headers)
    # result = BytesIO()
    # for chunk in res.iter_content(content_size):
    #     result.write(chunk)
    # return result.getvalue()
    return requests.get(url, headers=headers).content

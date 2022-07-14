import requests
from flask import Blueprint, request, make_response
from PIL import Image
import pillow_avif
from io import BytesIO
from tenacity import retry, stop_after_attempt

img_proxy = Blueprint("img_proxy", __name__)


def to_jpeg(img: bytes):
    result = Image.open(BytesIO(img)).convert('RGB')
    result_img = BytesIO()
    result.save(result_img, format="JPEG")
    return result_img.getvalue()


@img_proxy.route("/image_proxy")
def img_proxy_handler():
    resp = make_response(to_jpeg(downloader(request.args.get("url"))))
    resp.headers["Content-Type"] = "image/*"
    return resp


@retry(stop=stop_after_attempt(3))
def downloader(url, content_size=1024 * 128):
    headers = {"user-agent": 'Dart/2.10 (dart:io)'}
    res = requests.get(url, stream=True, headers=headers)
    result = BytesIO()
    for chunk in res.iter_content(content_size):
        result.write(chunk)
    return result.getvalue()

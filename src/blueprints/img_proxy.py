import requests
from flask import Blueprint, request, make_response
from PIL import Image
import pillow_avif
from io import BytesIO
from tenacity import retry, stop_after_attempt

img_proxy = Blueprint("img_proxy", __name__)


def to_jpeg(img: bytes):
    result = Image.open(BytesIO(img))
    result_img = BytesIO()
    result.save(result_img, format="JPEG")
    return result_img.getvalue()


@img_proxy.route("/res_image_proxy/<path:subpath>")
def res_img_proxy_handler(subpath: str):
    resp = make_response(to_jpeg(downloader(f"https://res.lightnovel.us{request.full_path.replace('/res_image_proxy', '')}")))
    resp.headers["Content-Type"] = "image/jpeg"
    return resp


@img_proxy.route("/noire_image_proxy/<path:subpath>")
def noire_img_proxy_handler(subpath: str):

    resp = make_response(to_jpeg(downloader(f"https://i.noire.cc{request.full_path.replace('/noire_image_proxy', '')}")))
    resp.headers["Content-Type"] = "image/jpeg"
    return resp


@retry(stop=stop_after_attempt(3))
def downloader(url, content_size=1024 * 128):
    headers = {"user-agent": 'Dart/2.10 (dart:io)'}
    res = requests.get(url, stream=True, headers=headers)
    result = BytesIO()
    for chunk in res.iter_content(content_size):
        result.write(chunk)
    return result.getvalue()

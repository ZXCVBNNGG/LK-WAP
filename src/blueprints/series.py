from flask import Blueprint, session, render_template

import src.blueprints.utils
from src.img_replace import img_replace
from . import s_api, db_session
from utils import get_user

series_page = Blueprint("series", __name__)


@series_page.route("/series/<sid>")
def series(sid: int):
    user = get_user(session)
    sid = int(sid)
    series_ = s_api.get_info(sid)
    return img_replace(render_template("series.html", user=user, series=series_))

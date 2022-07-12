from flask import Blueprint, session, render_template

from src.img_replace import img_replace
from . import s_api, db_session

series_page = Blueprint("series", __name__)


@series_page.route("/series/<sid>")
def series(sid: int):
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    sid = int(sid)
    series_ = s_api.get_info(sid)
    return img_replace(render_template("series.html", user=user, series=series_))
from flask import Blueprint, session, render_template

from src.img_replace import img_replace
from . import s_api, db_session, read_config
from .utils import get_user
from ..t_to_s import t_to_s, as_origin

series_page = Blueprint("series", __name__)


@series_page.route("/series/<sid>")
def series(sid: int):
    user = get_user(session)
    sid = int(sid)
    series_ = s_api.get_info(sid)
    read_c = read_config.get(-1 if not user else user.uid)
    t_to_s_func = t_to_s if read_c.global_force_simplified else as_origin
    return img_replace(render_template("series.html", user=user, series=series_, t_to_s=t_to_s_func))

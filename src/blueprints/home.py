from flask import Blueprint, render_template, session

import src.blueprints.utils
from . import db_session, c_api, PageSize, read_config
from ..t_to_s import t_to_s, as_origin
from .utils import get_user

home_page = Blueprint("home", __name__, template_folder='templates')


@home_page.route("/")
def home():
    user = get_user(session)
    read_c = read_config.get(-1 if not user else user.uid)
    t_to_s_func = t_to_s if read_c.global_force_simplified else as_origin
    category = c_api.get_categories(parent_gid=3)
    articles = c_api.get_article_by_cate(parent_gid=3, gid=106, page=1, pageSize=PageSize)
    return render_template("home.html", user=user,
                           category=category,
                           articles=articles,
                           t_to_s=t_to_s_func)

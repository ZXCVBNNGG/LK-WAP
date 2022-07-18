from flask import request, abort, session, render_template, Blueprint

import src.blueprints.utils
from pylkapi.models.response.category import Categories
from src.blueprints import c_api, PageSize, db_session, read_config
from src.t_to_s import t_to_s, as_origin
from .utils import get_user

category_page = Blueprint("category", __name__, template_folder='templates')


@category_page.route("/category/<gid>")
def category(gid: int):
    user = get_user(session)
    read_c = read_config.get(-1 if not user else user.uid)
    t_to_s_func = t_to_s if read_c.global_force_simplified else as_origin
    categories = c_api.get_categories(3)
    gid = int(gid)
    detail: None | Categories = None
    for i in categories:
        if i.gid == gid:
            detail = i
    if not detail:
        abort(500)
    page = request.args.get("page")
    if not page:
        page = 1
    articles = c_api.get_article_by_cate(3, gid, page, PageSize)
    sessionid = session.get("sessionid")
    return render_template("category.html",
                           a_detail=detail,
                           articles=articles,
                           user=user,
                           category=categories,
                           t_to_s=t_to_s_func)

from flask import request, abort, session, render_template, Blueprint

from pylkapi.models.response.category import Categories
from src.blueprints import c_api, PageSize, db_session

category_page = Blueprint("category", __name__, template_folder='templates')


@category_page.route("/category/<gid>")
def category(gid: int):
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
    user = db_session.get_user(sessionid=sessionid)
    return render_template("category.html", a_detail=detail, articles=articles, user=user, category=categories)

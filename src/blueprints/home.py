from flask import Blueprint, render_template, session

from . import db_session, c_api, PageSize

home_page = Blueprint("home", __name__, template_folder='templates')


@home_page.route("/")
def home():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    category = c_api.get_categories(parent_gid=3)
    articles = c_api.get_article_by_cate(parent_gid=3, gid=106, page=1, pageSize=PageSize)
    return render_template("home.html", user=user,
                           category=category,
                           articles=articles)

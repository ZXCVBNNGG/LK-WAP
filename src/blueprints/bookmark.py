from flask import Blueprint, render_template, session, request

from src.blueprints import db_session, h_api

bookmark_page = Blueprint("bookmark", __name__)


@bookmark_page.route("/bookmark")
def bookmark():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    if not user:
        return render_template("error.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    type_ = 1 if not request.args.get("type") else (1 if request.args.get("type") == "normal" else 0)
    page = 1 if not request.args.get("page") else int(request.args.get("page"))
    bookmark_ = h_api.get_collection(class_=class_, page=page, page_size=20, security_key=user.security_key,
                                     type_=type_, uid=user.uid)

    return render_template("bookmark.html", user=user,
                           bookmark=bookmark_,
                           h_class="article" if class_ == 1 else "series",
                           h_type="normal" if type_ == 1 else "other",
                           page_info=bookmark_.page_info)


@bookmark_page.route("/add_bookmark")
def add_bookmark():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    if not user:
        return render_template("error.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    fid = int(request.args.get("fid"))
    h_api.add_collection(class_, fid, security_key=user.security_key)
    return '添加成功！'


@bookmark_page.route("/del_bookmark")
def del_bookmark():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    if not user:
        return render_template("error.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    fid = int(request.args.get("fid"))
    h_api.del_collection(class_, fid, security_key=user.security_key)
    return '删除成功！'

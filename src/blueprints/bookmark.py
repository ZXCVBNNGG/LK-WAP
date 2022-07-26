from flask import Blueprint, render_template, session, request

import src.blueprints.utils

from src.blueprints import h_api, read_config
from .utils import get_user
from ..t_to_s import t_to_s, as_origin

bookmark_page = Blueprint("bookmark", __name__)


@bookmark_page.route("/bookmark")
def bookmark():
    user = get_user(session)
    if not user:
        return render_template("alert.html", message="请登录后使用！")
    read_c = read_config.get(-1 if not user else user.uid)
    t_to_s_func = t_to_s if read_c.global_force_simplified else as_origin
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    type_ = 1 if not request.args.get("type") else (1 if request.args.get("type") == "normal" else 0)
    page = 1 if not request.args.get("page") else int(request.args.get("page"))
    bookmark_ = h_api.get_collection(class_=class_, page=page, page_size=20, security_key=user.security_key,
                                     type_=type_, uid=user.uid)

    return render_template("bookmark.html", user=user,
                           bookmark=bookmark_,
                           h_class="article" if class_ == 1 else "series",
                           h_type="normal" if type_ == 1 else "other",
                           page_info=bookmark_.page_info,
                           t_to_s=t_to_s_func)


@bookmark_page.route("/add_bookmark")
def add_bookmark():
    user = get_user(session)
    if not user:
        return render_template("alert.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    fid = int(request.args.get("fid"))
    h_api.add_collection(class_, fid, security_key=user.security_key)
    return '添加成功！'


@bookmark_page.route("/del_bookmark")
def del_bookmark():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = src.blueprints.utils.get_user(sessionid)
    if not user:
        return render_template("alert.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    fid = int(request.args.get("fid"))
    h_api.del_collection(class_, fid, security_key=user.security_key)
    return '删除成功！'

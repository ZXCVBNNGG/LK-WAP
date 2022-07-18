from flask import Blueprint, render_template, session, request

import src.blueprints.utils
from src.blueprints import db_session, h_api
from .utils import get_user

history_page = Blueprint("history", __name__)


@history_page.route("/history")
def history():
    user = get_user(session)
    if not user:
        return render_template("alert.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    type_ = 1 if not request.args.get("type") else (1 if request.args.get("type") == "normal" else 0)
    page = 1 if not request.args.get("page") else int(request.args.get("page"))
    history_ = h_api.get_history(class_=class_,
                                 page=page,
                                 page_size=20,
                                 security_key=user.security_key,
                                 type_=type_,
                                 uid=user.uid)

    return render_template("history.html", user=user,
                           history=history_,
                           h_class="article" if class_ == 1 else "series",
                           h_type="normal" if type_ == 1 else "other",
                           page_info=history_.page_info)


@history_page.route("/del_history")
def del_history():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = src.blueprints.utils.get_user(sessionid)
    if not user:
        return render_template("alert.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    fid = int(request.args.get("fid"))
    h_api.del_history(class_, fid, security_key=user.security_key)
    return f'删除成功！'

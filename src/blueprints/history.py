from flask import Blueprint, render_template, session, request

from src.blueprints import db_session, h_api
from pylkapi.models.response.basic import SimplePageInfo

history_page = Blueprint("history", __name__)


@history_page.route("/history")
def history():
    session.permanent = True
    sessionid = session.get("sessionid") or ""
    user = db_session.get_user(sessionid)
    if not user:
        return render_template("error.html", message="请登录后使用！")
    class_ = 1 if not request.args.get("class") else (1 if request.args.get("class") == "article" else 2)
    type_ = 1 if not request.args.get("type") else (1 if request.args.get("type") == "normal" else 0)
    page = 1 if not request.args.get("page") else int(request.args.get("page"))
    history_ = h_api.get(class_=class_, page=page, page_size=20, security_key=user.security_key, type_=type_, uid=user.uid)

    return render_template("history.html", user=user,
                           history=history_,
                           h_class="article" if class_ == 1 else "series",
                           h_type="normal" if type_ == 1 else "other",
                           page_info=history_.page_info)
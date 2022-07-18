from flask import Blueprint, session, request, redirect, render_template

import src.blueprints.utils
from pylkapi.exception import PyLKApiException
from src.blueprints import u_api, db_session

login_page = Blueprint("login", __name__, template_folder='templates')


@login_page.route("/login", methods=['POST', 'GET'])
def login():
    session.permanent = True
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            r = u_api.login(username, password)
            db_session.add_user(r)
            sessionid = db_session.get_user(uid=r.uid).sessionid
            session["sessionid"] = sessionid
            return redirect("/")
        else:
            raise PyLKApiException(-1001)
    else:
        return render_template("login.html", user=None)

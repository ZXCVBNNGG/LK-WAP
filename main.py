from flask import Flask, render_template
from jinja2 import Environment
from requests.exceptions import HTTPError
from zhconv import convert
from src.blueprints.history import history_page
from src.blueprints.article import article_page
from src.blueprints.login import login_page
from src.blueprints.home import home_page
from src.blueprints.category import category_page
from src.blueprints.series import series_page
from src.blueprints.img_proxy import img_proxy
from src.blueprints.bookmark import bookmark_page

from pylkapi.exception import PyLKApiException

app = Flask(__name__)
jinja_env: Environment = app.jinja_env
app.config["SECRET_KEY"] = "1333a327-8cfb-4d72-a384-399d8962b263"  # a random uuid
app.register_blueprint(home_page)
app.register_blueprint(history_page)
app.register_blueprint(article_page)
app.register_blueprint(login_page)
app.register_blueprint(category_page)
app.register_blueprint(series_page)
app.register_blueprint(img_proxy)
app.register_blueprint(bookmark_page)


@app.errorhandler(HTTPError)
def handle_http_error(e: HTTPError):
    return render_template("error.html", message="LK服务器维护中！请耐心等待维护结束。")


@app.errorhandler(PyLKApiException)
def handle_lkapi_error(e: PyLKApiException):
    return render_template("error.html", message=f"API返回值与预期不符！错误代码：{e.code}")


def t_to_s(content: str):
    return convert(content, "zh-cn")


jinja_env.globals["t_to_s"] = t_to_s

if __name__ == "__main__":
    #    from werkzeug.middleware.profiler import ProfilerMiddleware

    #    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir="profiles")
    app.run()

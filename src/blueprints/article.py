from datetime import datetime, timezone, timedelta

from flask import Blueprint, request, render_template, session

from pylkapi.models.response.basic import SimplePageInfo
from src.blueprints import read_config, page_cache, s_api, a_api, h_api
from src.blueprints.utils import get_user, get_content_length, remove_img_tags
from src.pager import pager
from src.t_to_s import t_to_s, as_origin
from src.img_replace import img_replace

article_page = Blueprint("article", __name__, template_folder='templates')


def is_latest_of_article(aid: int, last_time: str):
    a = a_api.get_detail(aid, simple=1)
    return last_time == a.last_time


@article_page.route("/article/<aid>")
def article(aid: int):
    aid = int(aid)
    fulltext = False if not request.args.get("fulltext") else True
    page = 1 if not request.args.get("page") else int(request.args.get("page"))
    user = get_user(session)
    read_c = read_config.get(-1 if not user else user.uid)
    t_to_s_func = t_to_s if read_c.global_force_simplified else as_origin
    article_detail, content, fulltext, page_info = handle_content(aid, fulltext, page, read_c, user)
    series_page_info = handle_series(aid, article_detail, user)
    if user:
        h_api.add_history(1, aid, user.security_key)
    r_time = datetime.now(timezone(timedelta(hours=8))).strftime("%H:%M")
    return img_replace(render_template("article.html", detail=article_detail, time=r_time, page_info=page_info,
                                       series_page_info=series_page_info, content=content, user=user,
                                       fulltext=fulltext, t_to_s=t_to_s_func), compress=read_c.image_compress)


def handle_series(aid, article_detail, user):
    if article_detail.sid:
        series_page_info = get_series_page_info(aid, article_detail)
        if user:
            h_api.add_history(2, article_detail.sid, user.security_key)
    else:
        series_page_info = None
    return series_page_info


def handle_content(aid, fulltext, page, read_c, user):
    page_size = read_c.characters_num_per_page
    article_detail = get_article_detail(aid, user)
    length = get_content_length(article_detail.content)
    content_ = article_detail.content if not read_c.no_picture_mode else remove_img_tags(article_detail.content)
    if not fulltext:
        fulltext = False if length < read_c.auto_fulltext_num else True
    if not fulltext:
        contents = pager(content_, page_size)
        page_count = len(contents)
        page_info = SimplePageInfo(count=page_count, cur=page)
        content = contents[page - 1]
    else:
        page_info = SimplePageInfo(count=1, cur=1)
        content = content_

    return article_detail, content, fulltext, page_info


def get_article_detail(aid, user):
    article_detail = page_cache.get(aid)
    if not article_detail or not is_latest_of_article(aid, "" if not article_detail else article_detail.last_time):
        article_detail = a_api.get_detail(aid, "" if not user else user.security_key)
        page_cache.set(article_detail)
    return article_detail


def get_series_page_info(aid, article_detail):
    series_info = s_api.get_info(article_detail.sid)
    cur = series_info.articles.index(next((x for x in series_info.articles if x.aid == aid), None)) + 1
    s_next = series_info.articles[
        (len(series_info.articles) if cur == len(series_info.articles) else (cur + 1)) - 1].aid
    s_prev = series_info.articles[(1 if cur == 1 else (cur - 1)) - 1].aid
    has_next = 0 if aid == s_next else 1
    has_prev = 0 if aid == s_prev else 1
    series_page_info = SimplePageInfo(count=len(series_info.articles), cur=cur, next=s_next, prev=s_prev,
                                      has_prev=has_prev, has_next=has_next)
    return series_page_info

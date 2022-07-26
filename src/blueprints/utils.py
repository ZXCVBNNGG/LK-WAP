from bs4 import BeautifulSoup

from src.blueprints import db_session


def get_user(session):
    sessionid = session.get("sessionid")
    user = db_session.get_user(sessionid=sessionid)
    return user


def get_content_length(content: str):
    b = BeautifulSoup(content, features="lxml")
    return len(b.text)


def remove_img_tags(content: str):
    b = BeautifulSoup(content, features="lxml")
    for i in b.find_all("img"):
        i.extract()
    return str(b)
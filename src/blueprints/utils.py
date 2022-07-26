from bs4 import BeautifulSoup

from src.blueprints import db_session


def get_user(session):
    sessionid = session.get("sessionid")
    user = db_session.get_user(sessionid=sessionid)
    return user


def get_content_length(content: str):
    b = BeautifulSoup(content, features="lxml")
    return len(b.text)

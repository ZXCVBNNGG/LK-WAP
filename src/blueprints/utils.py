from src.blueprints import db_session


def get_user(session):
    sessionid = session.get("sessionid")
    user = db_session.get_user(sessionid=sessionid)
    return user

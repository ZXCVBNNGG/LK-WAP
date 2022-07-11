import uuid

from pydantic import BaseModel
from tinydb import TinyDB, Query

from pylkapi.models.response.user import LoginResponse


class SessionModel(BaseModel):
    sessionid: str
    uid: int
    nickname: str
    security_key: str


class Session:
    db = TinyDB("data/session.json")

    def is_exist(self, sessionid: str = None, uid: int = None, nickname: str = None):
        User = Query()
        if sessionid:
            return bool(self.db.search(User.sessionid == sessionid))
        if uid:
            return bool(self.db.search(User.uid == uid))
        if nickname:
            return bool(self.db.search(User.nickname == nickname))

    def add_user(self, user: LoginResponse):
        if self.is_exist(uid=user.uid):
            return
        sessionid = uuid.uuid4().hex
        self.db.insert(SessionModel(sessionid=sessionid,
                                    uid=user.uid,
                                    nickname=user.nickname,
                                    security_key=user.security_key).dict())

    def get_user(self, sessionid: str = None, uid: int = None) -> SessionModel | None:
        User = Query()
        if sessionid:
            result = self.db.search(User.sessionid == sessionid)
        else:
            result = self.db.search(User.uid == uid)
        if result:
            return SessionModel.parse_obj(dict(result[0]))
        else:
            return None

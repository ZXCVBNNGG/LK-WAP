from pylkapi.models.body.user import LoginBody, GetUserInfoBody
from .basic import BasicAPI
from .models.response.basic import BasicResponse
from .models.response.user import LoginResponse, OtherUser


class UserAPI(BasicAPI):
    def __init__(self):
        super().__init__()

    def login(self, username: str, password: str) -> LoginResponse:
        path = "/api/user/login"
        r = self._request(path, LoginBody(username=username, password=password))
        t = BasicResponse[LoginResponse].parse_obj(r)
        return t.data

    def get_user_info(self, uid: int, security_key=""):
        path = "/api/user/info"
        r = self._request(path, GetUserInfoBody(uid=uid, security_key=security_key))
        if security_key == "":
            t = BasicResponse[OtherUser].parse_obj(r)
        else:
            t = BasicResponse[LoginResponse].parse_obj(r)
        return t.data

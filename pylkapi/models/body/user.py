from .basic import BasicSubBodyModel


class LoginBody(BasicSubBodyModel):
    username: str
    password: str


class GetUserInfoBody(BasicSubBodyModel):
    uid: int
    security_key: str = ""

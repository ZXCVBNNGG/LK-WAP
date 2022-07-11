from .basic import BasicSubBodyModel


class GetDetailBody(BasicSubBodyModel):
    aid: int
    simple: int = 0
    security_key: str = ""

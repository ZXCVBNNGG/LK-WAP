from .basic import BasicSubBodyModel


class GetSeriesInfoBody(BasicSubBodyModel):
    sid: int
    security_key: str = ""

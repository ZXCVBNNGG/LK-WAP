from pydantic import Field

from .basic import BasicSubBodyModel


class AddHistoryBody(BasicSubBodyModel):
    class_: int = Field(..., alias='class')
    fid: int
    security_key: str


class GetHistoryBody(BasicSubBodyModel):
    class_: int = Field(..., alias='class')
    page: int
    page_size: int
    security_key: str
    type: int
    uid: int

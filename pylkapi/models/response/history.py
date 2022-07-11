from typing import List

from pydantic import BaseModel, Field

from .basic import BasicSubResponseModel, PageInfo
from .user import Level


class HistoryItemOfArticle(BaseModel):
    aid: int
    title: str
    banner: str
    uid: int
    _hits: int = Field(..., alias=' hits')
    comments: int
    time: str
    last_time: str
    cover: str
    cover_type: int
    gid: int
    parent_gid: int
    sid: int

class Editor(BaseModel):
    uid: int
    nickname: str
    avatar: str
    passer: int
    gender: int
    sign: str
    status: int
    banner: str
    ban_end_date: str
    level: Level

class HistoryItemOfSeries(BaseModel):
    sid: int
    name: str
    author: str
    banner: str
    cover: str
    cover_type: int
    rates: int
    last_time: str
    hits: int
    likes: int
    gid: int
    parent_gid: int
    group_name: str
    parent_group_name: str
    editors: List[Editor]



class GetHistoryResponse(BasicSubResponseModel):
    list: List[HistoryItemOfArticle | HistoryItemOfSeries]
    page_info: PageInfo

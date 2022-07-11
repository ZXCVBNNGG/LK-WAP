from typing import List

from pydantic import BaseModel

from .basic import BasicSubResponseModel
from .user import OtherUser


class Article(BaseModel):
    order: int
    aid: int
    title: str
    banner: str
    cover: str
    hits: int
    comments: int
    cover_type: int
    time: str
    last_time: str


class GetSeriesInfoResponse(BasicSubResponseModel):
    sid: int
    name: str
    gid: int
    parent_gid: int
    author: str
    intro: str
    banner: str
    rate: int
    cover: str
    cover_type: int
    rates: int
    last_time: str
    hits: int
    likes: int
    editors: List[OtherUser]
    score: int
    characters: List
    articles: List[Article]

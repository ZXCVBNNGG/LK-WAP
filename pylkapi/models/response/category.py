from typing import List, Optional

from pydantic import BaseModel

from .basic import BasicSubResponseModel, PageInfo


class Item(BaseModel):
    gid: int
    name: str
    logo: str
    cover_type: int
    order: int


class ArticleCates(BaseModel):
    gid: int
    name: str
    logo: str
    cover_type: int
    order: int
    items: Optional[List[Item]]


class GetArticleCatesResponse(BasicSubResponseModel):
    __root__: List[ArticleCates]


class Categories(BaseModel):
    gid: int
    name: str
    pic: str
    last_time: str


class GetCategoriesResponse(BaseModel):
    __root__: List[Categories]


class Article(BaseModel):
    aid: int
    banner: str
    cover: str
    title: str
    uid: int
    hits: int
    time: str
    last_time: str
    comments: int
    sid: int
    gid: Optional[int] = None
    group_name: Optional[str] = None
    cover_type: Optional[int] = None
    author: Optional[str] = None
    avatar: Optional[str] = None
    is_top: Optional[int] = None
    empty: Optional[int] = None


class GetArticleByCateResponse(BaseModel):
    list: List[Article]
    page_info: PageInfo

from typing import List, Optional

from pydantic import BaseModel

from .basic import BasicSubResponseModel


class Level(BaseModel):
    exp: int
    level: int
    name: str
    next_exp: int


class Balance(BaseModel):
    coin: int
    balance: int


class Medal(BaseModel):
    medal_id: int
    name: str
    desc: str
    type: int
    equip: Optional[int]
    expiration: Optional[str]
    img: str


class LoginResponse(BasicSubResponseModel):
    uid: int
    nickname: str
    avatar: str
    passer: int
    gender: int
    sign: str
    status: int
    banner: str
    ban_end_date: str
    medals: List[Medal | None]
    following: int
    comments: int
    favorites: int
    articles: int
    followers: int
    level: Level
    security_key: str
    balance: Balance


class OtherUser(BaseModel):
    uid: int
    nickname: str
    avatar: str
    passer: int
    gender: int
    sign: str
    status: int
    banner: str
    ban_end_date: str
    medals: List[Medal | None]
    following: int
    articles: int
    followers: int
    level: Level

from typing import List, Optional

from pydantic import BaseModel

from .basic import BasicSubResponseModel
from .user import OtherUser


class PayInfo(BaseModel):
    uid: int
    price_type: int
    price: int
    is_paid: int


class GetDetailResponse(BasicSubResponseModel):
    aid: int
    uid: int
    title: str
    summary: str
    content: str
    hits: int
    likes: int
    coins: int
    favorites: int
    comments: int
    shares: int
    time: str
    has_poll: int
    banner: str
    only_passer: int
    cover: str
    last_time: str
    lt: str
    gid: int
    parent_gid: int
    sid: int
    author: OtherUser
    other_recoms: List
    cache_ver: int
    only_app: int
    pay_info: Optional[PayInfo]
    already_coin: Optional[int]
    already_like: Optional[int]
    already_fav: Optional[int]
    already_follow: Optional[int]
    balance: Optional[List]

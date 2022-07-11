from typing import Literal

from .basic import BasicSubBodyModel


class GetArticleByCateBody(BasicSubBodyModel):
    parent_gid: int
    gid: int
    page: int
    pageSize: int
    security_key: str = ""


class GetArticleCatesBody(BasicSubBodyModel):
    depth: Literal[1, 2]
    cache: bool
    security_key: str = ""


class GetCategoriesBody(BasicSubBodyModel):
    parent_gid: int
    security_key: str = ""

from typing import List

from .basic import BasicAPI
from .models.body.category import GetArticleCatesBody, GetCategoriesBody, GetArticleByCateBody
from .models.response.basic import BasicResponse
from .models.response.category import GetArticleCatesResponse, GetCategoriesResponse, GetArticleByCateResponse, \
    Categories, ArticleCates


class CategoryAPI(BasicAPI):
    def __init__(self):
        super(CategoryAPI, self).__init__()

    def get_article_cates(self, depth: int, cache: bool, security_key="") -> List[ArticleCates]:
        path = "/api/category/get-article-cates"
        r = self._request(path, GetArticleCatesBody(depth=depth, cache=cache, security_key=security_key))
        t = BasicResponse[GetArticleCatesResponse].parse_obj(r)
        return t.data.__root__

    def get_categories(self, parent_gid: int, security_key="") -> List[Categories]:
        path = "/api/category/get-categories"
        r = self._request(path, GetCategoriesBody(parent_gid=parent_gid, security_key=security_key))
        t = BasicResponse[GetCategoriesResponse].parse_obj(r)
        return t.data.__root__

    def get_article_by_cate(self, parent_gid: int, gid: int, page: int, pageSize: int, security_key=""):
        path = "/api/category/get-article-by-cate"
        r = self._request(path, GetArticleByCateBody(parent_gid=parent_gid,
                                                     gid=gid,
                                                     page=page,
                                                     pageSize=pageSize,
                                                     security_key=security_key))
        t = BasicResponse[GetArticleByCateResponse].parse_obj(r)
        return t.data

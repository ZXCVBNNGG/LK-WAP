from .basic import BasicAPI
from .models.body.article import GetDetailBody
from .models.response.article import GetDetailResponse
from .models.response.basic import BasicResponse


class ArticleAPI(BasicAPI):
    def __init__(self):
        super(ArticleAPI, self).__init__()

    def get_detail(self, aid: int, security_key="", simple=0):
        path = "/api/article/get-detail"
        r = self._request(path, GetDetailBody(aid=aid, security_key=security_key, simple=simple))
        t = BasicResponse[GetDetailResponse].parse_obj(r)
        return t.data

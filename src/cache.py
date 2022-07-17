from tinydb import TinyDB, Query

from pylkapi.models.response.article import GetDetailResponse
from pylkapi.models.response.series import GetSeriesInfoResponse


class PageCache:
    db = TinyDB("data/page_cache.json")
    query = Query()

    def set(self, response: GetDetailResponse):
        self.db.insert(response.dict())

    def get(self, aid: int):
        r = self.db.search(self.query.aid == aid)
        if r:
            return GetDetailResponse.parse_obj(r[0])
        else:
            return None

    def remove(self, aid: int):
        self.db.remove(self.query.aid == aid)

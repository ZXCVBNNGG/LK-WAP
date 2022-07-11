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


class SeriesCache:
    db = TinyDB("data/series_cache.json")
    query = Query()

    def get(self, sid: int):
        r = self.db.search(self.query.sid == sid)
        if r:
            return GetSeriesInfoResponse.parse_obj(r[0])
        else:
            return None

    def set(self, response: GetSeriesInfoResponse):
        self.db.insert(response.dict())

    def remove(self, sid: int):
        self.db.remove(self.query.sid == sid)

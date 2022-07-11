from .basic import BasicAPI
from .models.body.series import GetSeriesInfoBody
from .models.response.basic import BasicResponse
from .models.response.series import GetSeriesInfoResponse


class SeriesAPI(BasicAPI):
    def __init__(self):
        super(SeriesAPI, self).__init__()

    def get_info(self, sid: int, security_key=""):
        path = "/api/series/get-info"
        r = self._request(path, GetSeriesInfoBody(sid=sid, security_key=security_key))
        t = BasicResponse[GetSeriesInfoResponse].parse_obj(r)
        return t.data

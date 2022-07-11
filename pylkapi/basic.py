from requests import Session

from pylkapi.models.body.basic import BasicSubBodyModel
from .models.body.basic import BasicBody


class BasicAPI:
    session = Session()
    root = "https://api.lightnovel.us"

    def __init__(self):
        self.session.headers["User-agent"] = "Dart/2.10 (dart:io)"
        self.session.headers["Content-Type"] = "application/json"

    def _request(self, path: str, model: BasicSubBodyModel) -> dict:
        r = self.session.post(self.root + path, data=BasicBody(d=model).json(by_alias=True))
        if r.status_code != 200:
            r.raise_for_status()
        return r.json()

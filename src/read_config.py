from pydantic import BaseModel
from tinydb import TinyDB, Query


class ReadConfigModel(BaseModel):
    uid: int
    characters_num_per_page: int
    image_compress: bool
    auto_fulltext: bool
    force_simplified: bool
    no_picture_mode: bool
    auto_fulltext_num: int



class ReadConfig:
    db = TinyDB("data/read_config.json")
    query = Query()

    def set(self, uid: int, characters_num_per_page: int):
        self.db.insert(ReadConfigModel(uid=uid, characters_num_per_page=characters_num_per_page).dict())

    def get(self, uid: int):
        r = self.db.search(self.query.uid == uid)
        if r:
            return ReadConfigModel.parse_obj(r[0])
        else:
            return None

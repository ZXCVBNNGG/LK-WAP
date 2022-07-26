from pydantic import BaseModel
from tinydb import TinyDB, Query


class ReadConfigModel(BaseModel):
    uid: int
    characters_num_per_page: int = 1000  # Done
    image_compress: bool = False  # Done
    auto_fulltext: bool = False  # Done
    global_force_simplified: bool = False  # Done
    no_picture_mode: bool = False  # Done
    auto_fulltext_num: int = 3000  # Done


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
            return ReadConfigModel(uid=-1)

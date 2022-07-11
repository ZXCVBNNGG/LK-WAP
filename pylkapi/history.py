from .basic import BasicAPI
from .models.body.history import *
from .models.response.basic import BasicResponse
from .models.response.history import *


class HistoryAPI(BasicAPI):
    def add(self, class_: int, fid: int, security_key: str):
        """
         :param class_: 历史分类 1：文章 2：合集
         :param fid: 文章或合集ID
         :param security_key: 用户KEY
        """
        path = "/api/history/add-history"
        r = self._request(path, AddHistoryBody.parse_obj({"class": class_, "fid": fid, "security_key": security_key}))
        t = BasicResponse[AddHistoryBody].parse_obj(r)
        return t.data

    def get(self, class_: int, page: int, page_size: int, security_key: str, type_: int, uid: int):
        """
        :param class_: 历史分类 1：文章 2：合集
        :param page: 页数
        :param page_size: 页面大小
        :param security_key: 用户KEY
        :param type_: 历史类别 0：其他 1：图书
        :param uid: 用户ID
        :return:
        """
        path = "/api/history/get-history"
        r = self._request(path, GetHistoryBody.parse_obj({"class": class_,
                                                          "page": page,
                                                          "page_size": page_size,
                                                          "security_key": security_key,
                                                          "type": type_,
                                                          "uid": uid}))
        t = BasicResponse[GetHistoryResponse].parse_obj(r)
        return t.data

    def get_collection(self):
        # TODO 收藏
        pass

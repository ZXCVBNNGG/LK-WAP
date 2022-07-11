from pylkapi import *
from src.cache import PageCache, SeriesCache
from src.read_config import ReadConfig
from src.session import Session

db_session = Session()
c_api = CategoryAPI()
u_api = UserAPI()
a_api = ArticleAPI()
s_api = SeriesAPI()
h_api = HistoryAPI()
page_cache = PageCache()
series_cache = SeriesCache()
read_config = ReadConfig()
PageSize = 40

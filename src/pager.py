from bs4 import BeautifulSoup
from .debug import clock


@clock
def pager(content: str, page_size: int):
    b = BeautifulSoup(content, features="lxml")
    results = []
    cache = ""
    count = 0
    for i in b.contents:
        if count >= page_size:
            results.append(cache)
            cache = ""
            count = 0
        cache = cache + str(i)
        count += len(i.get_text())
        if b.contents.index(i) == len(b.contents) - 1:
            results.append(cache)
            cache = ""
            count = 0
    return results

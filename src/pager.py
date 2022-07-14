from bs4 import BeautifulSoup
import cchardet
import functools
from .debug import clock


def real_contents_guess(b):
    if len(b.contents) > 1:
        return b.contents
    else:
        return real_contents_guess(b.contents[0])


@clock
@functools.cache
def pager(content: str, page_size: int):
    b = BeautifulSoup(content, features="lxml")
    real_contents = real_contents_guess(b)
    results = []
    cache = ""
    count = 0
    for i in real_contents:
        if count >= page_size:
            results.append(cache)
            cache = ""
            count = 0
        cache = cache + str(i)
        count += len(i.get_text())
    results.append(cache)

    return results

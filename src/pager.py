from typing import List

from bs4 import BeautifulSoup, NavigableString
import cchardet
import functools
from .debug import clock


def real_contents_guess(b):
    if len(b.contents) > 1:
        return b.contents
    else:
        return real_contents_guess(b.contents[0])


def final_child_tags_get(contents):
    child_tags = []
    for i in contents:
        if type(i) == NavigableString:
            child_tags.append(i)
            continue
        if len(i.contents) == 1 or len(i.contents) == 0:
            child_tags.append(i)
        else:
            child_tags.extend(final_child_tags_get(i.contents))
    return child_tags

@clock
@functools.cache
def pager(content: str, page_size: int):
    b = BeautifulSoup(content, features="lxml")
    real_contents = final_child_tags_get(real_contents_guess(b))
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

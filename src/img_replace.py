from bs4 import BeautifulSoup


def img_replace(content: str, compress=False):
    b = BeautifulSoup(content, features="lxml")
    for i in b.find_all("img"):
        if compress:
            url: str = "/image_proxy?url=" + i["src"]
        else:
            url: str = "/image_proxy?compress=true&url=" + i["src"]
        i["src"] = url
    return str(b)

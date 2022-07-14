from bs4 import BeautifulSoup


def img_replace(content: str):
    b = BeautifulSoup(content, features="lxml")
    for i in b.find_all("img"):
        url: str = "/image_proxy?url=" + i["src"]
        i["src"] = url
    return str(b)

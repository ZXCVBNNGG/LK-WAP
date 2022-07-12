from bs4 import BeautifulSoup


def img_replace(content: str):
    b = BeautifulSoup(content, features="lxml")
    for i in b.find_all("img"):
        url: str = i["src"].replace("https://res.lightnovel.us", "/res_image_proxy")\
            .replace("https://i.noire.cc", "/noire_image_proxy")
        i["src"] = url
    return str(b)

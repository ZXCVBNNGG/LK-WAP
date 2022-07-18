from zhconv import convert


def t_to_s(content: str):
    return convert(content, "zh-cn")

def as_origin(content: str):
    return content
import bbcode

parser = bbcode.Parser(replace_links=False)


def _render_size(tag_name, value, options, parent, context):
    return f'<span style="font-size:{options[tag_name]}px;">{value}</span>'


def _render_img(tag_name: str, value: str, options: dict, parent, context: dict):
    return f'<img src="{value}">'


def _render_align(tag_name: str, value: str, options: dict, parent, context: dict):
    return f'<span align="{options[tag_name]}">{value}</span>'


def _render_ruby(tag_name: str, value: str, options: dict, parent, context: dict):
    return f'<ruby><rb>{value}</rb><rp>(</rp><rt>{options[tag_name]}</rt><rp>)</rp></ruby>'


def _render_font(tag_name: str, value: str, options: dict, parent, context: dict):
    return f'<span style="font-family: "{options[tag_name]}"">{value}</span>'


parser.add_formatter("size", _render_size)
parser.add_formatter("img", _render_img)
parser.add_formatter("align", _render_align)
parser.add_formatter("ruby", _render_ruby)
parser.add_formatter("font", _render_font)


def content_to_html(content: str):
    return parser.format(content)

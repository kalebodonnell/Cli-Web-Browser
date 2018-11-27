from lxml import html

pages = {
    "duckduckgo.com": {
        "type": "search",
        "data-tag": "a",
        "data-class": "result-link"
    }
}


def get_page_items(page, data):
    parsed_data = html.fromstring(data)
    items = types[
        pages
        [page]
        ['type']
    ][0](page, parsed_data)

    return items


def get_search_items(page, data):
    page_data = pages[page]
    results = data.xpath('//{}[@class="{}"]'.format(
            page_data['data-tag'],
            page_data['data-class']
        )
    )
    out = []
    for i in results:
        out.append([
            i.text_content(),
            i.attrib['href']
        ])
    return out

def render_search_items(items):
    for idx,val in enumerate(items):
        print ("[{}] {}".format(idx,val[0]))
def render_page (page, items):
    types[pages[page]['type']][1](items)
types = {
    "search": [get_search_items,render_search_items]
}

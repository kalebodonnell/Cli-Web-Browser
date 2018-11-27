import requests
import pageTypes
import sys
import os

from urllib.parse import urlparse,parse_qs

query=input()
page="https://duckduckgo.com/lite/?q={}".format(query)


def get_page(page):
    r = requests.get(page)

    text = r.text
    domain = urlparse(r.url).hostname
    print ("{} : {}".format(
        text,
        domain
    ))

    items = pageTypes.get_page_items(domain,text)
    pageTypes.render_page(domain,items)

    user_in = input ("[0-{} or q]: ".format(len(items)-1))
    if (user_in == 'q'):
        exit()

    url = parse_qs(items[int(user_in)][1])['uddg'][0]
    if urlparse(url).hostname in pageTypes.pages:
        get_page(url)
    else:
        os.system('w3m "{}"'.format(url))
        get_page(page)

get_page(page)

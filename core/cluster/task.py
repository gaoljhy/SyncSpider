from requests import request
from cluster.celery import clus
from re import compile
# from json import dumps


@clus.task(name="http")
def creq(url, method, **kwargs):
    """ requests request
    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    """
    res = request(method, url,  **kwargs)
    return {res.status_code: res.content.decode("utf-8")}


@clus.task(name="regex")
def regex(stro, comp):
    """ re search 
    :param stro: origin text
    :param pattern: re complie object.
    """
    pattern = compile(comp)
    ll = pattern.findall(stro)
    result = ''
    l = 0
    for i in ll:
        l += 1
        result += str(l) + ' : ' + i + '\n'
    return result

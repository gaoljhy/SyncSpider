from cluster import creq, regex
from celery.result import AsyncResult


def runHttp(urls):
    """run some urls spider in sync
    :param url: urls link list
    """
    res = []
    for i in urls:
        res.append(creq.delay(url=i, method=method, headers=headers).id)
    return res


def runRe(res, comp):
    """run n task in re
    :param res: task id list
    """
    reg = []
    for i in res:
        reg.append(
            regex.delay(stro=AsyncResult(i).get()['200'], comp=comp).id
        )
    # print(reg)
    with open("out", "w") as f:
        j = 0
        for i in reg:
            j += 1
            strc = AsyncResult(i).get()
            f.write(' ---- ' + str(j) + ' - --- \n' + strc + '\n')

    print("结果写入文件完成...")


if __name__ == "__main__":
    comp = u'<h2>.*?</h2>'
    urls = ["http://cn.bing.com/search?q=se",
            "http://cn.bing.com/search?q=se&first=11",
            "http://cn.bing.com/search?q=se&first=21",
            "http://cn.bing.com/search?q=se&first=31", ]
    method = 'get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:68.0) Gecko/20100101 Firefox/68.0'}
    payload = {'q': "Opportunities"}
    # r = requests.get(url, headers=headers, params=payload)
    # print(r.content.decode('utf-8'))
    # print(r.status_code)
    res = runHttp(urls=urls)
    runRe(res=res, comp=comp)

# cli 接入接口
# api框架设计
# api 接入


# Celery 启动
# 后台启动
# celery multi start celery -A cluster

# 单独开启Queue
# celery multi start l1 -A cluster -l info -Q http
# celery multi start h1 -A cluster -l info -Q regex

# stop
# celery multi stop w3 -A cluster -l info

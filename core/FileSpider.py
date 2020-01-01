from core.scelery import creq, regex
from celery.result import AsyncResult


def runHttp(urls, method, headers):
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
    with open("out", "w") as f:
        j = 0
        for i in reg:
            j += 1
            strc = AsyncResult(i).get()
            f.write(' ---- ' + str(j) + ' - --- \n' + strc + '\n')

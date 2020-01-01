from core import runRe, runHttp

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
    res = runHttp(urls=urls, method=method, headers=headers)
    runRe(res=res, comp=comp,filepath="./")


# Celery 启动
# 后台启动
# celery multi start celery -A cluster

# 单独开启Queue
# celery multi start l1 -A cluster -l info -Q http
# celery multi start h1 -A cluster -l info -Q regex

# stop
# celery multi stop w3 -A cluster -l info

from scelery.task import creq, regex

# 后台启动
# celery multi start celery -A cluster

# 单独开启Queue
# celery multi start l1 -A cluster -l info -Q http
# celery multi start h1 -A cluster -l info -Q regex

# stop
# celery multi stop w3 -A cluster -l info

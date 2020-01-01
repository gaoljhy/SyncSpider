from kombu import Queue, Exchange

BROKER_URL = 'redis://172.17.0.1/0'
# 该 `broker` 参数为指定的中间人（Broker）URL。

# CELERY_RESULT_BACKEND = 'redis://172.17.0.1:6379/0'
# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://172.17.0.1/1'

# 该 `backend` 参数为指定的结果后端 `URL`。
# 它主要用于跟踪任务的状态的信息，默认情况下禁用结果后端，在此实例中已经开启了该功能
# 主要便于后续检索，可能在会在程序中使用不同的结果后端。
# 每一个后端都有不同的优点和缺点，如果不需要结果，最好禁用。
# 也可以通过设置 @task(ignore_result=True) 参数，针对单个任务禁用。
CELERY_TASK_SERIALIZER = 'json'  # 任务序列化和反序列化使用msgpack方案
CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

# 任务过期时间，不建议直接写，应该让这样的magic数字表述更明显
CELERY_TASK_RESULT_EXPIRES = 60 * 2
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

# 压缩方案选择，可以是 zlib, bzip2，默认是发送没有压缩的数据
CELERY_MESSAGE_COMPRESSION = 'zlib'

# 看了一篇文章说，如果使用redis做broker，exchange可以不配置；但如果使用rabbitMQ做broker，就必须要配置。
# 如果不配置队列，下面命令可以注释掉（简单的环境，建议不要配置）。
CELERY_QUEUES = {
    # Queue('default', exchange=Exchange(
    #     'default', type='direct'), routing_key='default'),
    Queue('http', exchange=Exchange(
        'http', type='direct'), routing_key='http'),
    Queue('regex', exchange=Exchange(
        'regex', type='direct'), routing_key='regex'),
}

CELERY_ROUTES = {
    # 匹配任务名以http开头的任何任务。
    'http': {'queue': 'http', 'routing_key': 'http'},
    # 精确匹配任务名称regex名称的任务，就匹配这条路由。
    'regex': {'queue': 'regex', 'routing_key': 'regex'},
}

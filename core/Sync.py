"""
指定规则以及配置进行部署 操作

# 后台启动
# scelery multi start scelery -A scelery

# 单独开启Queue
# scelery multi start l1 -A scelery -l info -Q http
# scelery multi start h1 -A scelery -l info -Q regex

# stop
# scelery multi stop w3 -A scelery -l info

"""
from os import system


def startUp():
    system("scelery multi start scelery -A scelery")


def setConfig():
    pass

from celery import Celery


clus = Celery('clus', include=['cluster.task'])

clus.config_from_object('cluster.config')


if __name__ == '__main__':
    clus.start()

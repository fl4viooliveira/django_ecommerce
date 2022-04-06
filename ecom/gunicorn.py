import os

bind: str = '0.0.0.0:8000'
backlog: int = 2048
workers: int = os.cpu_count() * 2 + 1
threads: int = 2
max_requests: int = 10

worker_class: str = 'gevent'

__all__ = ('bind', 'backlog', 'workers', 'threads', 'max_requests',)

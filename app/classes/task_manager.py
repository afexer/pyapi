from app.worker import start_worker
from rq import Queue


class TaskManager(object):
    conn = start_worker()
    q = Queue(connection=conn)

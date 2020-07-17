import redis
from rq import Worker, Queue, Connection


def start_worker():
    listen = ['default']
    redis_url = 'redis://localhost:6379'
    conn = redis.from_url(redis_url)

    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()


if __name__ == "__main__":
    start_worker()

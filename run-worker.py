import os
from redis import Redis
from rq import Queue, Connection
from rq.worker import HerokuWorker as Worker
from dotenv import load_dotenv
load_dotenv()

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL')
if not redis_url:
    raise RuntimeError('Set up Redis To Go first.')

conn = Redis.from_url(os.environ.get("REDIS_URL"))

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

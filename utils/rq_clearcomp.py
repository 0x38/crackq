import datetime
import rq
import sys

from rq import use_connection, Queue
from redis import Redis

redis_con = Redis('redis', 6379)
redis_q = Queue(connection=redis_con)

started = rq.registry.StartedJobRegistry('default',
                                         connection=redis_con)
failed = rq.registry.FailedJobRegistry('default',
                                       connection=redis_con)
comp = rq.registry.FinishedJobRegistry('default',
                                       connection=redis_con)
comp_list = comp.get_job_ids()
cur_list = started.get_job_ids()

#job_id = sys.argv[1]

#job = redis_q.fetch_job(job_id)
timestamp = datetime.datetime(2270, 1, 1)
print(timestamp)
comp.cleanup(timestamp=1000000)
comp_list = comp.get_job_ids()

print(comp_list)
#Queue.dequeue_any(redis_q, None, connection=redis_con)

#job = redis_q.fetch_job(job_id)
#print(job)



#多进程模块
from multiprocessing import Process
def f(text):
    print text, os.getpid()

print 'parent %s' % (os.getpid())
p = Process(target=f, args=('hello',))
p2 = Process(target=f, args=('world',))
p.start()
p2.start()
p.join()

import time,random
from multiprocessing import Pool, cpu_count
print cpu_count()

def task(name):
    print 'Run task %s on (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s needs %0.2f seconds' % (name, (end-start))

print 'start pool test'
p3 = Pool(5)
for i in range(5):
    p3.apply_async(task, args=(i,))
print 'wait'
p3.close()
p3.join()
print 'done'

print 'start pool test'
p3 = Pool()
for i in range(5):
    p3.apply_async(task, args=(i,))
print 'wait'
p3.close()
p3.join()
print 'done'

from multiprocessing.queues import Queue
def write(q):
    for i in [1,2,3]:
        print 'put %d in queue' % i
        q.put(i)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'get %d from queue' % value

q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
pw.start()
pr.start()
pw.join()
pr.join()
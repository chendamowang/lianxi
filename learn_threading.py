import threading, time
def loop():
    print 'thread %s is runing' % threading.current_thread().name
    n =1
    while n < 5:
        print 'thread %s ---  %d' % (threading.currentThread().name, n)
        n += 1
        time.sleep(1)
    print 'thread %s is ended' % threading.currentThread().name

print 'thread %s is runnig ' % threading.currentThread().name
t = threading.Thread(target=loop)
t.start()
t.join()
print 'thread %s is ended' % threading.currentThread().name

lock = threading.Lock()
threading.Lock()
a = 0
def change_it(n):
    global a
    a = a + n
    a = a - n
def run(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print a
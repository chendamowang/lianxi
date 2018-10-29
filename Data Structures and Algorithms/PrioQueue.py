# -*- coding:utf-8 -*-
"""
基于堆的优先队列
"""
class PrioQueueError(ValueError):
    pass


class PrioQueue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and elems[j] > e:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        e0 = self._elems[0]
        e = self._elems.pop()
        if len(self._elems) > 0:
            self.siftdown(e, 0, len(self._elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

# pq = PrioQueue(elist=[2,5,3,7])
# print pq.is_empty()
# pq.enqueue(1)
# print pq.dequeue()
# print pq.dequeue()
# print pq.peek()
# dd = float("inf")
# pq2 = PrioQueue(elist=[(2,'D'), (4,'A'), (1,'C'), (dd,'R')])
# print pq2.dequeue()
# print pq2.dequeue()
# print pq2.dequeue()
# print pq2.dequeue()
pq = PrioQueue()
pq.enqueue(3)
pq.dequeue()

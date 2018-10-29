# -*- coding: utf-8 -*-
"""
单链表python实现
"""
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head == None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        p = self._head
        if p is None:
            p = LNode(elem)
            return
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        p = self._head
        if p is None:
            raise ValueError("in pop_last")
        if p.next is None:
            e = p.elem
            p = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def insert(self, i, elem):
        if i >= self.__len__():
            raise LinkedListUnderflow("out of index")
        p, n = self._head, 0
        while p is not None:
            n += 1
            if n == i:
                p.next = LNode(elem, p.next)
            p = p.next

    def remove(self, i):
        if i >= self.__len__():
            raise IndexError("out of index")
        p, n = self._head, 0
        while p is not None:
            n += 1
            if n == i:
                p.next = p.next.next
            p = p.next

    def __len__(self):
        p, n = self._head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def print_all(self):
        p = self._head
        while p is not None:
            if p.next is None:
                print p.elem
            else:
                print p.elem,
            p = p.next

    def __getitem__(self, i):
        p, n = self._head, 0
        while p is not None:
            n += 1
            if n == i:
                return p.elem
            p = p.next

list1 = LList()
for i in range(5):
    list1.prepend(i)
list1.append(8)
list1.append(9)
list1.print_all()
print len(list1)
print list1.pop()
print list1.pop_last()
list1.print_all()
list1.insert(1,9)
list1.print_all()
list1.remove(1)
list1.print_all()
print list1[3]
for x in list1.filter(lambda x: x%2 == 0):
    print x,
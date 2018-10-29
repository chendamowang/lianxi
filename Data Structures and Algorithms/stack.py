# -*- coding: utf -8 -*-
class StackUnderflow(ValueError):
    pass


#栈的顺序表实现
class SStack(object):
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return  self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()


#栈的链接表实现
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LStack(object):
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


# st1 = SStack()
# st1.push(1)
# st1.push(5)
# print st1.pop()
# print st1.pop()
#
# st2 = LStack()
# st2.push(2)
# st2.push(4)
# print st2.pop()
# print st2.pop()
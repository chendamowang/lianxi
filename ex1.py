#! user/bin/python
# -*- coding:utf-8 -*-
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


class test(object):
    def f(self, a):
        n = 0 
        for i in a:
            for j in a:
                for k in a:
                    if i != j and i != k and j != k:
                        print i,j,k
                        n += 1
        print '总数是: %d' % n
        

if __name__ == '__main__':
    test1 = test()
    a = [1,2,3,4]
    test1.f(a)                                         

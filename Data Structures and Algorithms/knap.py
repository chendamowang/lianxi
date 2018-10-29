# -*- coding: utf-8 -*-
"""
背包问题：一个背包可放入重量为weight的物品,现有n件物品的合集S,
其中物品的重量分别为w0,w1,...,wn-1。是否能从中选出若干物品,
其重量刚好等于weight
"""

def knap_res(weight, wlist, n):
    if weight == 0:
        return  True
    if weight < 0 or (weight > 0 and n == 0):
        return False
    if knap_res(weight-wlist[n-1], wlist, n-1):
        print 'Item' + str(n) + ':', wlist[n-1]
        return True
    if knap_res(weight, wlist, n-1):
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]
weight = 10
knap_res(weight, a, len(a))
from copy import copy, deepcopy

a = [1,2,3,['a','b']]

b = a[:]
c = a
d = copy(a)
e = deepcopy(a)

a.append(3)
a[3].append('c')

print a
print b
print c
print d
print e


print range(5,0,-1)
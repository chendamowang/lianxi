# -*- coding: utf-8 -*-
#collections模块练习
from collections import namedtuple
Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y


from collections import defaultdict
a = defaultdict(lambda : 'nihao')
print a['ss']


from collections import  deque
b = deque(['a','b', 'c'])
b.append('s')
b.appendleft('z')
print b


from collections import OrderedDict
od = OrderedDict()
od['d'] = 'd'
od['a'] = 'z'
print od.keys()
from collections import Counter


#装饰器练习
import functools
def log(fuc):
    @functools.wraps(fuc)
    def wrapper(*args, **kwargs):
        print "这是装饰器"
        fuc(*args, **kwargs)
    return  wrapper
@log
def now():
    print  'nihaoya'
now()

def log2(text):
    def decorator(fuc):
        @functools.wraps(fuc)
        def wrapper(*args, **kwargs):
            print "%s %s()" % (text, fuc.__name__)
            fuc(*args, **kwargs)
        return  wrapper
    return  decorator

@log2('call')
def now():
    print 'hello'

now()


#re模块练习
import re
phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
m = phoneregex.search('my numer is 123-245-241')
print m.group()

#() 分组
phoneregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
m = phoneregex.search('my numer is 123-245-241 and 123-432-555')
print m.group()
print m.group(1)
print m.group(2)

# | 管道
heroregex = re.compile(r'Batman|Tina Fey')
n = heroregex.search('Batman and Tina Fey')
print n.group()
n2 = heroregex.findall('Batman and Tina Fey')
print n2

#?可选 或非贪心
nogreedyharegex = re.compile(r'(ha){3,5}?')
n = nogreedyharegex.search('hahahahahaha')
print n.group()

#匹配邮箱
emailRegex2 = re.compile(r'^[a-z][a-zA-Z0-9_]*@[a-zA-Z0-9_-]+(\.com)')
m = emailRegex2.search('chenweizhe@163.com')
print m.group()



#os 模块
import  os
print os.path.join('user','bin')
a=  os.getcwd()
print os.path.abspath('.')
print os.listdir('.')
print os.path.getsize('./learn.py')
for foldername, subfolders, filenames in os.walk(a):
    print foldername
    for subfolder in subfolders:
        print subfolder
    for filename in filenames:
        print filename




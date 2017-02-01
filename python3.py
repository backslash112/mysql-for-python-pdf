#!/usr/bin/env python

#
# This module is a example list. (Say something to show the module's behavior)
#

def func(a, b, c):
    return a + b + c

# PEP 3107 Function Annotations: 函数注释
def func2(a: 'spam', b: (1,10), c: float) -> int:
    return a + b + c


def dog(name, gender, age):
    print(name)
# 调用：
dog('Lucy', 'F', 2)

# PEP 3102 Keyword-only Arguments: 强制关键字
def dog2(name, gender, *, age):
    print(name)
# 调用：
dog('Lucy', 'F', age = 2)

def sayhi(name):
    print('hi {0}!'.format(name))

# Use the backslash(\) to separete one line to multi-line code.
def sayhi2():
    if 1 > 2 and \
       2 > 3:
       print('hi')
    else:
        print('hehe')

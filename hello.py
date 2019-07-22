#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/22 11:10
@File    : hello.py 
'''

'''
def hello(words):
    print('hello', words)


hello('world')
'''

import cProfile


def loop(count):
    result = []
    for i in range(count):
        result.append(i)


cProfile.run('loop(10000)')
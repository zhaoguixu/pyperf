#!/usr/bin/python
# _*_ coding:utf-8 _*_

__author__ = 'root'

import time


start = time.time()

print sum([x for x in range(1, 10000)])

elapsed1 = time.time() - start

print elapsed1

start = time.time()
print sum(x for x in range(1, 10000))

elapsed2 = time.time() - start

print elapsed2

print (elapsed1 - elapsed2) / elapsed1




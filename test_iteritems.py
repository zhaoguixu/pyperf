#!/usr/bin/python
# _*_ coding:utf-8 _*_

__author__ = 'root'

import time


x = {}
for i in range(1, 10000000):
    x[i] = str(i)


start = time.time()

y = {}

for k, v in x.items():
    y[k] = v

elapsed1 = time.time() - start

print elapsed1

start = time.time()
z = {}
for k, v in x.iteritems():
    z[k] = v

elapsed2 = time.time() - start

print elapsed2

print (elapsed1 - elapsed2) / elapsed1

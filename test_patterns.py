#!/usr/bin/python
# _*_ coding:utf-8 _*_

__author__ = 'root'

users = [1, 2, 3]

user_ids1 = set([user for user in users])

user_ids2 = {user for user in users}

x = [user for user in users]
user_ids3 = set(x)
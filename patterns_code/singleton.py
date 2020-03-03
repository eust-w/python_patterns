#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:singleton.py
@time:2020/02/28
"""


class Singleton(object,):
    def __init__(self):
        self.a = self
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            # 反射
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)   # <__main__.Singleton object at 0x004415F0> <__main__.Singleton object at 0x004415F0>
print(obj1 is obj2)

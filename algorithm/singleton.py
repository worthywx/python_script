# -*- coding: utf-8 -*-
# Author: Worthy
# Create Time: 2017/11/8 16:27

class SingleTon(object):
    """使用类实现单例模式"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class S(SingleTon):
    pass


def singleTon(cls):
    """装饰器实现单例模式"""
    instance = {}

    def wrapper(*args):
        if cls not in instance:
            instance[cls] = cls(*args)
        return instance[cls]

    return wrapper


@singleTon
class A(object):
    def __init__(self, val):
        self.val = val

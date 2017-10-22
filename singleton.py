#coding=utf-8
#单例模式实现方式

from threading import Lock
from random import choice
lock = Lock()

class Singleton(object):
    '''__new__实现单例模式'''
    _instance = None

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                lock.acquire()
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            finally:
                lock.release()
        return cls._instance

def singletonDecorator(cls, *args, **kwargs):
    '''装饰器版本单例模式'''
    instances = {}
    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singletonDecorator
class A(object):
    score = 5

a = A()
b = A()
print id(a) == id(b)

def test_singleton_in_thread():
    '''测试单例模式线程安全'''
    seq = ['a', 'b', 'c', 'd', 'e']
    inst = Singleton(choice(seq))
    print inst.name
    print id(inst)

#-*- coding: utf-8 -*-
#Author: Worthy
#Create Time: 2017/11/17 13:40

from weakref import WeakKeyDictionary

class NoneNegative(object):
    def __init__(self, val):
        self.default = val
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed")
        self.data[instance] = value


class Movie(object):
    budget = NoneNegative(0)
    gross = NoneNegative(0)

    def __init__(self, title, budget, gross):
        self.title = title
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget

a = Movie("Hero", 8, 10)

print a.profit()
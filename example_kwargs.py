#!/usr/bin/python
# coding: utf8

def listArgs(*args):
    for i in args:
        print(i)

def listKwargs(**kwargs):
    for i in kwargs:
        print(i)

listArgs('a', 'b', 'c')
listKwargs(a=5, b=10)

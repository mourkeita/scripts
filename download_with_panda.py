#!/usr/bin/python
# coding: utf8


import pandas

print("Downloading website ")

res = pandas.read_html('https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor')
print(res[8])
print(res[10])


for i in range(len(res)):
    print('****** ', i, ' ********', end=' ')
    print(res[i])
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:20:21 2021

@author: Saurabh Jain
"""

days = int(input())
limit = 2

def fun(attendance, last_a, limit, days):
    if last_a == limit+1:
        return [0,0]
    if attendance == days:
        if last_a == 0:
            return [0,1]
        else:
            return [1,1]
    attendance += 1
    result_a = fun(attendance, last_a+1, limit, days)
    result_p = fun(attendance, 0, limit, days)
    return [result_a[0] + result_p[0], result_a[1] + result_p[1]]

result = fun(0,0, limit, days)

print(f"({result[1]}, {result[0]}/{result[1]})")
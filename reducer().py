'''
=> reduce() in Python is a higher-order function from the functools module. It’s used to reduce a sequence of elements into a single cumulative value by repeatedly applying a specified function.

=> package name : from functools import reduce
=> syntax : reduce(function, iterable, initializer)
'''

from functools import reduce

numbers = [13,42,66,94,14,86,16]

def fun(a,b):
    return a+b

sum = reduce(fun,numbers)

print(sum)
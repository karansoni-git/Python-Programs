'''
=> The filter() function in Python is used to filter elements from an iterable (like a list, tuple, or set) based on a condition (a function that returns True or False).
-> syntax : filter(function, iterable)
'''

numbers = [32,52,76,89,13,57,35,90,83]

odd = list(filter(lambda x : x % 2 !=0 , numbers))

print(odd)
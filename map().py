'''
=> What is map()?
-> map() is a built-in function that applies a given function to each item of an iterable (like list, tuple, etc.).
-> It returns a map object (which is an iterator).

=> syntax : map(function, iterable)
'''
l = [2,4,6,8,10]

square = lambda x:x*x

# normal function also can use in map function
# def square(x):
#     return x*x

sqlist = list(map(square,l))
print(sqlist)

# here we have defined the defintion of function inside the map function
cube_list = list(map(lambda x : x*x*x , l))
print(cube_list)
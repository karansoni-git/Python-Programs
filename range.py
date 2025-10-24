'''
In Python, the range() function is used to generate a sequence of numbers. It is  commonly used in loops (especially for loops) to iterate over a sequence of numbers.
by default range start from 0 index and does not include the last number of the range

| Parameter | Description                            | Default  |
| --------- | -------------------------------------- | -------- |
| `start`   | The starting number of the sequence    | 0        |
| `stop`    | The end of the sequence (not included) | Required |
| `step`    | The difference between each number     | 1        |

range() returns a range object, which is an immutable sequence of numbers. You can convert it to a list
'''
print("range(stop) : ")
for i in range(5):
    print(i , end=" ")

print("\n\nrange(start,stop) : ")
for i in range(11,16):
    print(i ,end=" ")

print("\n\nrange(start,stop,step) : ")
for i in range(1,10,2):
    print(i ,end=" ")

print("\n\nrange converted to list : ")
x = range(1,6)
newtuple = list(x)
print(newtuple)

print("\nrange converted to tuple : ")
newtuple = tuple(x)
print(newtuple)
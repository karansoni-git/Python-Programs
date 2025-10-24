# Replication Operator: (*) 
# Replication operator uses two parameter for operation. One is the integer value and the other one 
# is the String. 
# The Replication operator is used to repeat a string number of times. The string will be repeated 
# the number of times which is given by the integer value.

print("karan " * 3)

# Membership Operators 

# 1) in: return true if a character or the entire substring is present in the specified 
# string, otherwise false. 
print("k" in "karan")

# 2) not in: return true if a character or entire substring does not exist in the 
# specified string, otherwise false. 
print("s" not in "soni")

# Relational Operators: 
# All the comparison operators i.e., (<,><=,>=,==,!=,<>) are also applicable to strings. The Strings 
# are compared based on the ASCII value or Unicode(i.e., dictionary Order). 
result = "k"=="K"
print(result)

# Slice Notation: 
# String slice can be defined as substring which is the part of string. 
# start index in String slice is included whereas end index is excluded. 
# Syntax: 
# string-name[startIndex:] print from given start index to all characters
# string-name[:endIndex], print from 0 index to given end index
# string-name[startIndex:endIndex], print from start given index to end given index where end index is not include

str = "karan soni"
slicestr = str[2 : 5]
print(slicestr)

# negative slicing
print(str[-4 : -1])

# slicing with step
print(str[0 : 5 : 2])  #index 0 to 5 and with 2 step(character)
print(str[0 : : 2]) #index 0 to last index and with 2 step(character)

#advance slicing 
print(str[0:]) 
print(str[:5]) 

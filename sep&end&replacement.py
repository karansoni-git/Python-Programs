# the sep (short for separator) is an optional parameter used in the print() function to specify how multiple items are separated when printed.
print("karan","nishit","dhruvil","krish",sep=" * ")
print(9,7,2025,sep="/")

# the end parameter (often called an attribute) is used in the print() function to specify what to print at the end of the line, instead of the default newline (\n).
print("karan",end="🧠\n")
print("soni")

# format() : allows value replacement using format() or f-strings.
name = "karan"
surname = "soni"
print("my first name is {} and lastname is {}".format(name,surname))

# f-string
print(f"hy i am {name} and my surname is {surname}")
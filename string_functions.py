# string functions are used to manipulate and process strings.
# one thing that you have to remember is that string is immutable so the string will be same as it before any operations

str1 = "Karan Soni"
str2 = "python programming"

# str.lower() : Converts all characters to lowercase.
print("lower() : ",str1.lower()) 

# str.upper() : Converts all characters to uppercase.
print("upper() : ",str2.upper())

# str.capitalize() : Converts the first character of the string to uppercase
print("capitalize() : ",str2.capitalize())

# str.title() : Converts the first character of each word to uppercase.
print("title() : ",str2.title())

# str.swapcase() : Swaps the case of each character (upper → lower and vice versa).
print("swapcase() : " ,end="")
print("KaRaN sONi".swapcase())

# str.casefold() : More aggressive lowercasing (used for caseless comparisons).
print("casefold() : " ,end="")
print("India Is VEry BEST".casefold())

# str.strip() : Removes leading(left side) and trailing(right side) spaces.
print("strip() : " ,end="")
print("     Breaking Bad     ".strip())

# str.lstrip() : Removes leading spaces.
print("lstrip() : " ,end="")
print("     Breaking Bad     ".lstrip())

# str.rstrip() : Removes trailing spaces.
print("rstrip() : " ,end="")
print("     Breaking Bad     ".rstrip())

# str.zfill(width) : Pads the string on the left with zeros to make it width characters long.
# If the string is already equal to or longer than width, it's returned unchanged.

print("zfill() : " ,end="")
print("example".zfill(10))

# str.ljust(width, fillchar=' ') : Left aligns the string and fills extra space with fillchar
print("ljust() : " ,end="")
print("left".ljust(10,"*"))

# str.rjust(width, fillchar=' ') : Right aligns the string.
print("rjust() : " ,end="")
print("right".rjust(10,"*"))

# str.center(width, fillchar=' ') : Centers the string.
print("center() : " ,end="")
print("center".center(12,"*"))

# str.find(sub) : Returns index of first occurrence of sub, or -1 if not found.
print("find() : " ,end="")
print("stringi".find("i"))

# str.rfind(sub) : Same as find() but from the right. -1 if not found.
print("rfind() : " ,end="")
print("stringi".rfind("i"))

# str.index(sub) : Like find(), but raises ValueError if not found.
print("index() : " ,end="")
print("hello".index("l"))

# str.rindex(sub) : Like rfind(), but raises error if not found.
print("rindex() : " ,end="")
print("hello".rindex("l"))

# str.count(sub) : Returns number of occurrences of sub in the string.
print("count() : " ,end="")
print("ram ram jay raja ram".count("ram"))

# sub in str : Returns True if sub is found in str.
print("in : " , end="")
print("kar" in "karan parekh")


# str.isalpha() : Checks if all characters are alphabets.
print("isalpha() : " ,end="")
print("sample".isalpha())

# str.isdigit() : Checks if all characters are digits in string.
print("isdigit() : " ,end="")
print("1234".isdigit())

# str.isalnum() : Checks if all characters are alphanumeric (alphabets and numeric values only no symbols)
print("isalnum() : " ,end="")
print("karan".isalnum())

# str.islower() : Checks if all characters are lowercase.
print("islower() : " ,end="")
print("Python is not only snake".islower())

# str.isupper() : Checks if all characters are uppercase.
print("isupper() : " ,end="")
print("IT IS A language also".isupper())

# str.isspace() : Checks if string contains only whitespace.
print("isspace() : " ,end="")
print(" ".isspace())

# str.istitle() : Checks if string is in title case.
print("istitle() : " ,end="")
print("I Am Batman".istitle())

# str.startswith(prefix,start(optional),end(optional)) : Checks if string starts with prefix.
print("startswith() : " ,end="")
print("I love Python".startswith("I love"))

# str.endswith(suffix,start(optional),end(optional)) : Checks if string ends with suffix.
print("endswith() : " ,end="")
print("I love Python".endswith("thon"))

# str.replace(old, new, count(optional)) : Replaces all occurrences of old with new.
print("replace() : " ,end="")
print("good good morning".replace("good","nice"))

# str.split(seperator, maxsplit) : Splits string into list using separator sep.
print("split() : " ,end="")
print("python is coming".split(" "))

# str.rsplit(seperator, maxsplit) : Splits from the right.
print("rsplit() : " ,end="")
print("right,side,split,is,working".rsplit(","))

# str.splitlines() : Splits at line breaks.
print("splitlines() : " ,end="")
print("hello\nworld".splitlines())

# str.partition(sep) : Splits into 3 parts: before sep, sep, after sep.
print("partition() : " ,end="")
print("left:right".partition(":"))

# str.rpartition(sep) : Like partition() but from the right.
print("rpartition() : " ,end="")
print("hello google google i am fine".rpartition("google"))

# join() : is used to join (combine) a list of strings into a single string, using a specified separator
print("join() : " ,end="")
print(" & ".join(["karan","krish","dhruvil"]))

# str.encode(encoding) : Returns encoded version of the string (e.g., UTF-8).
print("encode() : " ,end="")
print("love python".encode())

# str.format() : Performs string formatting (replaces {} with values).
print("format() : " ,end="")
print("name : {} age : {}".format("karan",20))

# f"{var}" : f-string formatting
print("f{var}() : " ,end="")
print(f"surname : {"soni"}")
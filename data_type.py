# int (Integer)
# Stores: Whole numbers (positive or negative)
# Is Mutable: No (immutable)
int_var = 10

# float (Floating Point)
# Stores: Decimal numbers
# Is Mutable: No
float_var = 20.41

# complex
# Stores: Complex numbers in form a + bj
# Is Mutable: No
complex_var = 3+4j

# str (String)
# Stores: Text (sequence of characters)
# Is Mutable: No
string_var = "Karan"

# bool
# Stores: True or False
# Is Mutable: No
boolean_var = True

# list
# Stores: Ordered collection of items (can be of mixed types)
# Mutable
list = [10,20,30]

# tuple
# Stores: Ordered, fixed-size collection
# Immutable
tuple = (40,50,60)

# range(start, stop, step)
# used to generate a sequence of numbers
range = range(5)

# dict (Dictionary)
# Stores: Key-value pairs
# Mutable
dictionary = {"name" : "karan" , "age" : 20}

# set
# Stores: Unordered collection of unique items
# Is Mutable: Yes (elements must be immutable)
set = {"parekh" , "gondal"}

# frozenset
# Stores: Immutable set
# Immutable
frozenset = frozenset({"karan","nishit","dhruvil","jay"})

# NoneType
# Stores: A null value (represents nothing)
none = None

print("integer : " , int_var)
print("float : " , float_var)
print("string : " , string_var)
print("complex : " , complex_var)
print("real part : ",complex_var.real)
print("imaginary part : ",complex_var.imag)
print("boolean : " , boolean_var)
print("list : " , list)
print("tuple : " , tuple)
print("range : " , range)
print("dictionary : " , dictionary)
print("set : " , set)
print("frozenset : " , frozenset)
print("None : " , none)

print("\nall Type of data : \n")

print("integer : " , type(int_var))
print("float : " , type(float_var))
print("string : " , type(string_var))
print("complex : " , type(complex_var))
print("boolean : " , type(boolean_var))
print("list : " , type(list))
print("tuple : " , type(tuple))
print("range : " , type(range))
print("dictionary : " , type(dictionary))
print("set : " , type(set))
print("frozenset : " , type(frozenset))
print("set : " , type(none))


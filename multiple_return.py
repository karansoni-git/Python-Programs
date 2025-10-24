# Function that returns multiple values
def calculate_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined"
    
    # Returning multiple values as a tuple
    return addition, subtraction, multiplication, division

# Taking input
x = 10
y = 5

# Calling the function
add, sub, mul, div = calculate_operations(x, y)

# Displaying results
print(f"For numbers {x} and {y}:")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
 
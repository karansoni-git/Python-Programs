def reverse(n):
    n_str = str(n)[::-1]
    return int(n_str)

num = int(input("Enter a number : "))
print(reverse(num))


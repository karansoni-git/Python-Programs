def check(c):
    if (c == 'a' or c == 'i' or c == 'e' or c == 'o' or c == 'u'):
        print(f"{c} is vowel")
    else:
        print(f"{c} is not vowel")

char = input("Enter a Character : ").lower()
check(char)
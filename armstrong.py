def armstrong(n):
    s = 0
    while(n > 0):
        r = n % 10
        s = (r*r*r) + s
        n = n // 10
    return s

c = int(input("enter number:"))
if(armstrong(c) == c):
    print(f"number {c} is armstrong")
else:
    print(f"number {c} is not armstrong!")

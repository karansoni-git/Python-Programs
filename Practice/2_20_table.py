def table(num):
    with open(f"table_{num}.txt","w") as f:
        f.write(f"Table of {num} :\n")
        for i in range(1,11):
            f.write(f"{num} X {i} : {num*i}\n")

table(2)
table(14)
table(19)

with open("sample1.txt","r") as r:
    content = r.read()

with open("sample2.txt","w") as w:
    w.write(content)


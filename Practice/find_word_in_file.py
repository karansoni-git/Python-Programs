with open("reading_file.txt","r") as f:
    content  = f.read().lower()
    word = "Karan"
    if (word.lower() in content):
        print("find it")
    else:
        print("can not find it")
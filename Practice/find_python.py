# word that we want to find
word = "python"
# open the file and fetch lines
with open("python.txt","r") as f:
    lines = f.readlines()

# define the lineno
lineno = 1 

# findind the word in single line
for line in lines:
    if(word in line):
        print(f"{word} is find in line no {lineno}")
        break #break loop when found the word
    lineno += 1 # incrementing the lineno if word not found in current line
else:
    print(f"{word} is not find in file")
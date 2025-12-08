word_list = ["bad","kill","gun","rascal","mad"]

# read the file first
with open("censored.txt","r") as f:
    content = f.read()
    
# replce the original content where the word occurs that is present in the word_list
for i in word_list:
    content = content.replace(i,"*" * len(i))

# rewrite the file with updated content
with open("censored.txt","w") as f:
    f.write(content)


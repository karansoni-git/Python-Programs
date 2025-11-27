'''
=> opens a file in reading mode. it is ok if we don't mention the read mode because open() function open a file by default in read mode.
-> If the file is located in a different location, you will have to specify the file path, like this: '''
file = open("reading_file.txt","r")


''' read(size) : is used to read the content of a file as a string.
If size is not given, it reads the entire file. '''
# full_content = file.read()

# read only 30 characters from file
# some_content = file.read(30)


''' readline(size (optional) ) : is used to read one line at a time from a file.
-> size → Max number of characters to read. If omitted or -1, reads the whole line.
-> Returns a string containing the line (including the \n at the end).
-> Returns an empty string "" when the end of file (EOF) is reached. '''
# single_line = file.readline()
# single_line_size = file.readline(5)


# readlines() : reads all lines from a file and returns them as a list of strings.
lines_list = file.readlines()

file.close()


# print(full_content)
# print(some_content)
# print(single_line)
# print(single_line_size)
print(lines_list)
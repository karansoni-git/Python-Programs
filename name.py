'''
=> What is __name__ in Python?
-> __name__ is a special built-in variable in every Python module (file).
-> It tells how the module is being executed:
-> If the file is run directly, __name__ == "__main__"
-> If the file is imported as a module, __name__ == module_name
'''

def sample():
    print("sample code in name file (module)")
    print(f"Module Name : {__name__}")

# always shows __main__ when you run this program

# shows the file name when you use this module in other file

def data():
    if __name__ == "__main__":
        print("This is an important data which can see by admin")
    else:
        print("You dont have permission to see the data!")
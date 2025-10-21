"""
here we have add a module name pyjokes 
how can we install someone modules to our programs?
=> using pip3 , you just have to write a pip3 install module-name
here it goes like : pip3 install pyjokes    
"""
# import the pyjokes module using import statement
import pyjokes

# here we have the used the get_joke() function of the pyjokes module
print(pyjokes.get_joke())
# dir() is used to list out all function name of any module
# print(dir(pyjokes))
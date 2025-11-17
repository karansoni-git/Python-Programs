import pylab

fruits = ['apples','banana','grapes','guava','cherry']
sales = [99,17,86,58,43]


pylab.bar(fruits,sales,color="magenta",width=0.8,align='center')
pylab.title("fruits sales graph")
pylab.xlabel("fruits categories")
pylab.ylabel("fruits sales")

pylab.show()
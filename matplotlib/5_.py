import pylab

labels = ["iphone","samsung","oppo","google","vivo","iqoo"]
values = [1.1,1.01,0.7,0.65,0.57,0.89]
colors = ["green","yellow","red","blue","magenta","navy"]

pylab.pie(values,labels=labels,shadow=True,colors=colors)
pylab.title("MOBILE SOLD IN 2025")

pylab.show()
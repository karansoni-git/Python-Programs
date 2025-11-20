import pylab
principal = 10000  # initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
    
pylab.title('5% Growth, Compounded Annually',fontsize='smaller')
pylab.xlabel('Years of Compounding',fontsize='xx-large')
pylab.ylabel('Value of Principal ($)',fontsize='smaller')
pylab.plot(values,"--",linewidth=2)
pylab.show()

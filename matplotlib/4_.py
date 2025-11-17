import pylab

x1 = [160, 165, 170, 175, 180, 185, 190, 195, 200, 205]
y1 = [55, 58, 60, 62, 64, 66, 68, 70, 72, 74]

x2 = [150, 155, 160, 165, 170, 175, 180, 195, 200, 205]
y2 = [50, 52, 54, 56, 58, 64, 66, 68, 70, 72]

pylab.scatter(x1, y1, color='blue', label='Group 1',edgecolors="black",marker='^')
pylab.scatter(x2, y2, color='red', label='Group 2',edgecolors="green",marker="p")
pylab.xlabel('Height (cm)')
pylab.ylabel('Weight (kg)')
pylab.title('Comparison of Height vs Weight between Two Groups')
pylab.legend()
pylab.show()

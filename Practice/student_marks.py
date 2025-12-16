student = 1
marks = []
while student <= 6:
    mark = int(input("Enter mark : "))
    marks.append(mark)
    student +=1
marks.sort()
print(marks)

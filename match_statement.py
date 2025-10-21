'''
=> what is Match statement?
-> The match statement is used to perform different actions based on different conditions.
-> Instead of writing many if..else statements, you can use the match statement.
-> The match statement selects one of many code blocks to be executed.

=> Default Value
-> Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
'''
try:
    day = int(input("Enter the day in number : "))
except ValueError:
    print("Please Enter Value In Number")
else:
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")  
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Nothing Match")

# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
# You can add if statements in the case evaluation as an extra condition-check:
month = 5
match day:
    case 2|3|4|5|6:
        print("Today Is Working Day")
    case 1|7 if month == 4:
        print("Today Is Holiday")


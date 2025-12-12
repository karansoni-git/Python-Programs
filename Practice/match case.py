name = input("enter the first character of your name : ").lower()

match name:
    case 'k':
        print("karan".upper())
        print("krish".upper())
    case 'v':
        print("vedant".upper())
        print("vatsal".upper())
    case 'd':
        print("dhruvil".upper())
        print("dev".upper())
    case 'a':
        print("anant".upper())
    case 's':
        print("somya".upper())
    case 'n':
        print("nishit".upper())
    case 'b':
        print("bhavya".upper())
    case _:
        print("Nothing Match!")



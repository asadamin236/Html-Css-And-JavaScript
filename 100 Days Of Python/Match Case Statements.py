X = int(input("Enter a number"))

match X:
    case 0:
        print("X is 0")
    case 4:
        print("X is 4")

    case _ if X !=90:
        print(X, "X is not equal to 90")
    case _ if X != 80:
        print(X, "X is not equal to 80")

    case _:
        print(X)
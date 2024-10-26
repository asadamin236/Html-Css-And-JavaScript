try:
    list1 = [1, 2, 4, 6, 7]

    i = int(input("Enter the index: "))
    print(list1[i])
except:
    print("Some error occurred")

finally:
    print("I am always executed")
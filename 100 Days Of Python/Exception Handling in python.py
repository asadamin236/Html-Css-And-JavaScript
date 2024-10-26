A = input("Enter a number: ")
print(f"Multiplication table of {A} is: ")
try:
    for i in range(1, 11):
        print(f"{int(A)} x {i} = {int(A)*i}")
except Exception as e:
    print("Invalid Input")

print("Some important line of code")
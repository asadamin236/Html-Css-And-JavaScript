# If else statement
A = int(input("Enter Your Age"))
print("Your age is:", A)

if(A >= 18):
    print("You are eligible for NIC Creation")
else:
    print("You are not eligible")

# Nested if statement

B = int(input("Enter your marks"))
print("Your Marks Is:", B)

if(B >= 80):
    print("You pass with A Grade")
elif(B >= 70 and B <=79):
    print("You pass with B Grade")
elif(B >= 50 and B <= 69):
    print("You pass with C Grade")
else:
    print("Sorry you are fail")
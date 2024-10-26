tup = (1, 2, 3)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])

if  3 in tup:
    print("Yes present in tuple")

else:
    print("Not Present")

Tup1 = ("Pak", "Ind", "Nz", "Aus")
temp = list(Tup1)
temp[2] = "USA"
temp[3] = "Ban"
print(tuple(temp))

tup3 = (1,1,2,2,2,3,4,5,6)

print(tup3.count(1))
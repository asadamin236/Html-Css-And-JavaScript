list1 = ["Orange", "Apple", "Pear", "Banana", "Kiwi", "Apple", "Banana"]

print(list1.count("Apple"))
print(list1.index("Banana", 4))

print(list1.reverse())
print(list1)
list1.append("Graps")
print(list1)
list1.sort()

print(list1)

list1.pop()
print(list1)
list1.remove("Apple")
print(list1)

del list1[1: 2]
print(list1)

for x in list1:
    a =[]
    a.append(x)
    print(a)
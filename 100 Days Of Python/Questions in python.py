## Question No 1: Ek list banayein jisme 10 random numbers ho. Unhe print karein.
import random
list1 = [2, 3, 5, 7, 8, 9, 2, 5, 9, 10]
print(list1)
## Question No 2: Program for even number
Even_Number = []

for num in list1:
    if num %2 == 0:
        #print(num)
        Even_Number.append(num)

print("Even Number =",Even_Number)

## Question No 3: Combine two lists
list2 = [11, 12, 13, 14]

# Combine two lists
list3 = list1 + list2
print(list3)

## Question No 4: Sort list in descending order.
list4 =[]
list3.sort(reverse=True)
list4.append(list3)

print("Sorted list in descending order:", list4)

## Question No 5: Remove Duplicate values from list
list5 = list(set(list1))

print("Unique Numbers:", list5)

### Tuples

Tup1 = ("Amir", "Asad", "Aqib", "ALi", "Saqib")

print(Tup1[1])

print(list(Tup1))

Tup2 = (2, 3, 5, 6, 10)
print(min(Tup2), max(Tup2))

Tup3 = ("Asad", 25, "Python Developer")

name, age, profession = Tup3
print(Tup3)
print("Name: ", name)
print("Age: ", age)
print("Profession: ", profession)

## Dictionary
Dict1 = {"Amir": 90, "Asad": 80, "Aqib": 85, "Adil": 82}
print(Dict1)

print(Dict1["Asad"])

## Update new item in Dictionary
Dict1.update({"Ali": 70})
print(Dict1)

## Remove item from dictionary
Dict1.pop("Ali")
print(Dict1)
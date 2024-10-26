# Dict1 = {1: "Amir", 2: "Asad", 3: "Zeeshan", 4: "Adnan"}
#
# del Dict1[1]
# print(Dict1)
# for i in Dict1.values():
#     print(i)
# print(len(Dict1))
#
# for keys, values in Dict1.items():
#     print("Keys: ", keys, "Values: ", values)
#
# for key in Dict1.keys():
#     print(key)
#
# Dict1.clear()
# print(Dict1)

Dict2 = {1: "Amir", 2: "Asad", 3: "Zeeshan", 4: "Adnan"}

print(Dict2[1])

print(Dict2.get(1))

print(Dict2.pop(1))
print(Dict2)
Dict3 = {1, "Amir"}

Dict2.update(Dict3)

print(Dict2)
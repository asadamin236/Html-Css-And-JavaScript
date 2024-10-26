Dict1 = { 25: "Asad Amin",
          26: "Amir",
          27: "Aqib"}
print(Dict1)
print(Dict1.keys())
print(Dict1.values())
for key in Dict1.keys():
    print(Dict1[key])

print(Dict1.items())

## Update in Dictionary

Dict2 = {28: "Saqib", 29: "Adil", 30: "Ali"}

Dict1.update(Dict2)
print(Dict1)
Dict3 = {28: "Saqib", 29: "Adil", 30: "Ali"}
print(Dict3)

## Clear Method in Dictionary use for clear dict
Dict3.clear()
print(Dict3)

Dict1.popitem()
del Dict3[30]
print(Dict3)
# List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(List1[1:10:2])
# i =0
# List2 = [for i in range(20)]
# print(List2[1:15:2])
Dict1 = {}
List2 = ["A", "B", "C"]
List3 = ["a", "b", "c"]

for k, v in enumerate(List2):
    Dict1[v] = List3[k]

print(Dict1)
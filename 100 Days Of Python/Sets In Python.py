S = {1,2,3}
print(type(S))
Dict1 = {"Amir": 1, "Asad": 2, "Ali": 3, "Khan": 4}
print(Dict1.values())
S2 = {3, 4, 5}
S3 = {3, 4, 5}
S4 = {3, 4, 5}

print(S.union(S2))
print(S.intersection(S2))
print(S2.intersection_update(S))
print(S.difference(S2))
print(S2.issuperset(S))
print(S4.issubset(S3))
print(S4.add(6))
print(S4)
print(S4.remove(6))
print(S4)
# empty set:
e = set()
print(type(e))
# sets:
s = {20,56,21,20,20,20} # reptetive values doesn't count in sets
print(type(s))
print(s)

# 1 - add function:
s.add(97969)
print(s)

# 2- union for to join/intersect two sets:
s1 = {45,21,11,89,1}
s2 = {56,88,32,45,1,11,78}
print(s1.union(s2))
print(s1.intersection(s2)) #only common values

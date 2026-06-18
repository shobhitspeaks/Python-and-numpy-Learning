# empty dictionery :
d = {} 
# dictionary:
age = {
    "Shobhit" : 20, 
    "Parth" : 35,
    "Sachin": 23
}
print(type(age))
# dictionery is mutable it contains key and Values:

print(age["Sachin"])

# 1 - .items fucntion:
print(age.items())

# 2 - update key and values:
age.update({"Parth" : 19})
print(age)

# 3- pop function:
age.pop("Shobhit")
print(age)
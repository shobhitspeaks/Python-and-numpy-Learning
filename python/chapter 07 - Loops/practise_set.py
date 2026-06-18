# 1- multiplication table using for loop:
n = int(input("enter your number: "))
for i in range(1,21):
    print(f"{n} x {i} = {n*i}")

# 2 - greet all names in a list which starts with s:
l = ["Harry" , "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"GoodMorning {name}")

# 3 - multiplication using while loop:
n = int(input("enter your number: "))

i = 1 
while(i<21):
    print(f"{n} x {i} = {n*i}")
    i += 1
  
# 4 - check prime number:
num = int(input("enter your number: "))
for i in range(2,num):
    if(num%i) == 0:
        print("it it not a prime number")
        break

else:
    print("it is a prime number")


# 5 - factorial:
# 5! = 1x2x3x4x5 
num = int(input("enter your num: "))
product = 1
for i in range(1,num+1):
    product = product*i

print(f"the factorial of {num} is {product}")

# 6 - reverse multiplication table:
n = int(input("enter your number: "))
for i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")

# 11 is the sum of table numbers like-
# 1 10 = 11
# 2 9 = 11
# 3 8 = 11
# 4 7 = 11
# 5 6 = 11
# 6 5 = 11
# 7 4 = 11
# 8 3 = 11
# 9 2 = 11
# 10 1 = 11
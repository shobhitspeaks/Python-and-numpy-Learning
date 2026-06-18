# 1 - write a programm to find greatest of three numbers 
#     using functions:

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c ):
        return b 
    elif(c>a and c>b):
        return c
    
a = 5
b = 8 
c = 34

print(greatest(a,b,c))
        
# 2 -  how to avoid new line in python:

print("Shobhit")
print("Shiva")
print("Lakshya")
print("Sakshi")     #NORMAL PRINT

print("Shobhit")
print("Shiva")
print("Lakshya",end="")
print("Sakshi", end="")  # PRINT IN ONE LINE


# 3 - PATTERN:

def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

# 4 - inches to cms:

def inches_to_cms(inch):
    return inch * 2.54

n = int(input("enter a number: "))
print(f"the coverted value of inch into cms is: {inches_to_cms(n)}")
    
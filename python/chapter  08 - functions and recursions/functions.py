# we can create our own function to do some repetitive work:

def avg():
    n1 = int(input("enter your number 1: "))
    n2 = int(input("enter your number 2: "))
    n3 = int(input("enter your number 3: "))
    
    avg = (n1+n2+n3)/3
    print(avg)

avg() # this is function call

# functions with arguments:

def greet(name , Ending):
    print("Good Morning," + name )
    print(Ending)

greet("Shobhit", "Have a Good Day")

# Return term:

def greet(name , Ending):
    print("Good Morning," + name )
    print(Ending)
    return "See You Later!"

R = greet("Shobhit", "Have a Good Day")
print(R)
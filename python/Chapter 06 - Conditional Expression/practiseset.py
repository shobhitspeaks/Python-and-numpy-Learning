# 1 -write a programm to find greatest number of four entered by user:
# a1  = int(input("enter your number 1 : "))
# a2  = int(input("enter your number 2 : "))
# a3  = int(input("enter your number 3 : "))
# a4  = int(input("enter your number 4 : "))

# if(a1>a2 and a1>a3 and a1>a4 ):
#     print("greatest number is:", a1)

# elif(a2>a1 and a2>a3 and a2>a4 ):
#     print("greatest number is:", a2)

# elif(a3>a1 and a3>a2 and a4>a3 ):
#     print("greatest number is:", a3)

# elif(a4>a1 and a4>a3 and a4>a2 ):
#     print("greatest number is:", a4)


# 2 - student marks pass or fail:

# m1 = int(input("enter marks 1: "))
# m2 = int(input("enter marks 2: "))
# m3 = int(input("enter marks 3: "))

# total_perecentage = (100*(m1+m2+m3))/300

# if(total_perecentage>=40):
#     print("Congratualtions!, You are passed",total_perecentage)

# else:
#     print("You are Failed, Better Luck next time",total_perecentage)

#3 - spam comment detect:

# p1 = "Make a lot of money"
# p2  ="Buy now"
# p3 = "Subscribe this"
# p4 = "Click this"

# message = input("Enter your comment: ")

# if (p1 in message or p2 in message or p3 in message or p4 in message):
#     print("This is a spam comment")

# else:
#     ("this is not a spam comment")

# 4- write a programm to identify character is 10 or less:

username = input("enter your username: ")
# print(username)
# print(len(username))

if(len(username)>10):
    print("it contains more than 10 characters",len(username))

else: 
    print("it is contains less than 10 characters",len(username))
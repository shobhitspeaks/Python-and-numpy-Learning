# for loop: 
for i in range(1,11):
    print(i)

# while loop (conditions in loops):
i = 1
while(i<6):
    print(i)
    i +=1

# step size (a gap between range):
for i in range(1,101,5):  #( 5 is a step size a gap in series)
    print(i)

# for loops with else:
l = [29,89,98,112]  #List
for item in l:
    print(item)
else:
    print("all values printed successfully")
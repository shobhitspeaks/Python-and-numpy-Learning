'''
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 2 x 1
Factorial(3) = 3 x 2 x 1
Factorial(4) = 4 x 3 x 2 x 1
Factorial(5) = 5 x 4 x 3 x 2 x 1

Factorial(n) = n x n-1 x .......3 x 2 x 1

Factorail(n) = n * Factorial(n-1)

'''

def Factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * Factorial(n-1)

n = int(input("enter a number: "))
print(f"the factorial of this numbers is: {Factorial(n)}")
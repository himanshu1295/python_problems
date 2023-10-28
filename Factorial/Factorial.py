# Given an integer N. Write a program to return the factorial of N.
# Note: 0 factorial is equal to 1.

def nFactorial():
    
    n = int(input("Enter a number: "))
    
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    print(ans)

nFactorial()

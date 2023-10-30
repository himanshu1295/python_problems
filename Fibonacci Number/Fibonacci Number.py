'''
Given an integer n. Write a program to find the nth Fibonacci number.
The nth Fibonacci number is given by the forumla F(n)=F(n-1)+F(n-2). The first few fibonacci numbers are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ..... and so on
'''

def fibonacci(n):
    a = 0                       # starts with a = 0 at the first index which is 0
    b = 1                       # starts with b = 1 at the second index which is 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):   # when the whole loops runs from 2 to n+1 then only value is returned
            c = a + b             
            a = b                 # a becomes b , eg.  a = 2 and b = 3 now c = 5 so a will become 3 and b will become 5
            b = c                 # b becomes c
        return b                  # value of b is returned which is in the series
 
print(fibonacci(9))   # at 9th place or index 34 is present in the fibonacci series
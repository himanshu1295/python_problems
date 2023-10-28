# Given an integer n check if n is prime or not.
# A prime number is a number that is divisible by 1 and itself only.

def isPrime():
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Not a prime number")

    for i in range(2, int(n ** 0.5) + 1):           # Loop through all numbers from 2 to the square root of n 
        if n % i == 0:                              # (rounded down to the nearest integer)
            print("Not a prime number")
            break
    else:
        print("Prime number")

isPrime()

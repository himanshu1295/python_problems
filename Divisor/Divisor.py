# Given an integer N. Write a program to print all the divisors of N.

def divisor():
    n = int(input("Enter a Number: "))

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end = " ")

divisor()


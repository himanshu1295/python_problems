# Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

def reverse():
    x = int(input("Enter a Number: "))

    while x >= 0:
        print(x, end = " ")
        x -= 1

reverse()

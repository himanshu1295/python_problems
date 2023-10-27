# Given an integer s,  write a program to print the square wall of size s using single loops. Use * character to make the wall.

def print_square():
    s = int(input("Enter the size of the square: "))

    for i in range(s):
        print("* " * s)

print_square()
# Given an integer s,  write a program to print a square wall of size s without using string multiplication. 
# Use nested loops instead. The * character will make up the wall.

def SquareWall():
    s = int(input("Enter the Size of the Square: "))

    for i in range(s):
        for j in range(s):
            print("*", end = "")
        print()

SquareWall()

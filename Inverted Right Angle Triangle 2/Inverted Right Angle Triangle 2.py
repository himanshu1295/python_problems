# Given an integer s. Write a program to print the Inverted "Right angle triangle" wall. 
# The length of the perpendicular and base is s. Use double loop.

def InvertedTriangle():
    s = int(input("Enter the length of the perpendicular and base: "))

    for i in range(s, 0, -1):         # start at i = 4 and end at i = 0 
        for j in range(i):            # start at j = 4 and end at j = 0
            print("*", end=" ")
        print()                       # in double for loop always remember to use print() for new line

InvertedTriangle()

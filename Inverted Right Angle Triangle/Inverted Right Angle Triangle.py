# Given an integer s. Write a program to print the Inverted "Right angle triangle" wall. 
# The length of the perpendicular and base is s.  Use a single loop and string multiplication.

def InvertedTriangle():
    s = int(input("Enter the length of the perpendicular and base of the inverted triangle: "))

    for i in range(s, 0, -1):
        print("* " * i)

InvertedTriangle()
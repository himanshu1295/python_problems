# Given an integer s. Write a program to print the Right angle triangle wall. 
# The length of perpendicular and base is s.  Use single loop and string multiplication.

def TriangleWall():
    s = int(input("Enter the Size of the Triangle: "))

    for i in range(1, s+1):
        print("* " * i)

TriangleWall()

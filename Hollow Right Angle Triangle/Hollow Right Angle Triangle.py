# Given an integer s. Write a program to print the Hollow Right Angle Triangle. 
# The length of the perpendicular and base is s.  
# Use single loop and string multiplication.

def triangle():
    s = int(input("Enter the length of the perpendicular and base of the triangle: "))

    for i in range(s):
        if i == 0:
            print("*")
        elif i == s - 1:           # last range - 1 will give full length boundary
            print("* " * s)        
        else:
            print("*" + str(" " * (i * 2)) + "*")  # i * 2 multiply 'space' between the 2 stars.

triangle()
        
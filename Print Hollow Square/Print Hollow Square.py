# Given an integer s, write a program to print the hollow square of size s using * character.

# Method 1 :

def hollowSquare():
    s = int(input("Enter the size of the hollow square: "))
    for i in range(s):
        if i == 0:
            print("*" * s)
        elif i == s - 1:
            print("*" * s)
        else:
            print("*" + str(" " * (s - 2)) + "*")     # s-2 because hollow spaces in between leaving 1st and last
hollowSquare()

########################################################################

# Method 2 :

def square():
    s = int(input("Enter the size of the hollow square: "))
    
    for i in range(s):
        for j in range(s):
            if i == 0 or i == s - 1 or j == 0 or j == s - 1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()                                 # prints new line when the j value is increased

square()
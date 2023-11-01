# Given a string s, you need to slice it so that the output is a substring that contains all the chracters except first and last. 
# The length of the s will be greater than 2.

def SliceString():
    s = input("Enter a string: ")

    result = s[1:len(s)-1]  # can also be written as s[1:-1] where it starts from 1 and -1 is the last alphabetic character

    print(result)

SliceString()
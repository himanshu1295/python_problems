# Given a string s, you need to perform the following operation.

# 1. Capitalize the first letter and print.
# 2. Convert the whole string to uppercase and print.

def ChangeCase():
    s = input("Enter a string: ")

    print(s.title())  # can also be used s.capitalize() to capitalize the first letter
    print(s.upper())

ChangeCase()
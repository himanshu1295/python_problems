# Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line.

def Alphabet():
    c1 = input("Enter a character: ")
    c2 = input("Enter another character: ")

    a = ord(c1)
    b = ord(c2)

    for i in range(a, b + 1):
        print(chr(i), end=" ")

Alphabet()

'''
can also be used written as :

for i in range(ord(c1), ord(c2) + 1):
    print(chr(i), end="")
'''

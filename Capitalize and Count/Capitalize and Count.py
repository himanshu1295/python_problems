# Given a string s of single space-separated words. 

# Capitalize the first letter of all words and count the number of the words in the string.

def CapitalizeWords():
    s = input("Enter a string: ")

    print(s.title())

    words = s.split()
    
    print(len(words))

CapitalizeWords()

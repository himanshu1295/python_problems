# Given a string s, you need to check if it is palindrome or not. 
# A palidrome is a string that reads the same from front and back. Ignore the case in this question.

def IsPalindrome():
    s = input("Enter a string: ")
    s = s.lower()
    s1 = s[::-1]
    
    if s == s1:
        print("True")
    else:
        print("False")

IsPalindrome()

# Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s. 
# If p does not exist in s then -1 will be returned.
# Here p and s both are case-sensitive.

s = input("Enter a String: ")

p = input("Enter a pattern: ")

def FindPattern(s, p):
    pos = s.find(p)     # This will return the starting index of the pattern
    print(pos)

FindPattern(s, p)

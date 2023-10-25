'''
Logical operators and, or, not are used in condition checking. 

Like a and b checks if both a and b are True. First a is checked then b is checked. 

a or b checks if either of a or b is True. If one is True; it doesn't check for the other.

not a complements the boolean value of a

Note: 0 and empty string are False and all other values are True.

Task: In this question you basically need to do :
1.) a and b
2.) a or b
3.) not a
'''

a = int(input("Enter value of a: "))

b = int(input("Enter value of b: "))

p = a and b

q = a or b

r = not a

print("Output of {} and {} is {}".format(a, b, p))

print("Output of {} or {} is {}".format(a, b, q))

print("Output of not {} is {}".format(a, r))

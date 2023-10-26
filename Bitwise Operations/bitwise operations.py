'''
Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b          # and
4. g = c | (a ^ a)    # or
5. h = ~ e            # not
Note: ^ is for xor.
'''

def bitwise_operations():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    c = int(input("Value of c: "))

    d = a ^ a
    e = c ^ b
    f = a & b
    g = c | (a ^ a)
    h = ~ e

    print(d, e, f, g, h)

bitwise_operations()

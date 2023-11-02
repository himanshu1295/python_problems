# Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.

def solution(a, b):
    temp = a          # storing the value of a in temp
    a = b             # storing the value of b in a (swapping the values)
    b = temp          # now assigning the value of temp to b

    print(a, b)

solution(2, 3)
'''
Given four inputs that are stored in variables a,b,c, and d. 

You need to write an expression to evaluate the following formula : (a+b)/c + d

Use integer division. The expression should be a single statement.
'''

def expression():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    c = int(input("Value of c: "))
    d = int(input("Value of d: "))

    result = ((a + b) / c) + d

    print(result)

expression()
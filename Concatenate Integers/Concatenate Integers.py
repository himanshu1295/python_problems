# Given two integers a and b, you need to concatenate them so the output is ab.

def utility():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # to concatenate the two numbers we need to convert integer to a string

    ans = str(a) + str(b)

    print(ans)

utility()
# Given two numbers A and B. The task is to find the GCD of  A and B.
# The GCD of two numbers is the largest number that can divide both A and B perfectly.

def gcd(a, b):
        
    # Find minimum of a and b
    result = min(a, b)
 
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
 
    # Return the gcd of a and b
    return result

print(gcd(6, 9))

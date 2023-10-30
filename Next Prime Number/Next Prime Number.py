# Given an integer n. Write a program to find the prime number next to n.

n = int(input("Enter the number: "))

def nextPrime(n):
    num = n + 1                            
    while not is_prime(num):      # if the below result is false then while loop becomes True and num will increment
        num += 1                  # then while loop will run again
    return num                    # if the below result = True, then while loop = False, then value return 'num' which is prime number
    
def is_prime(n):                  # to check if number is prime or not
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(nextPrime(n))        # return value needs to be printed hence using print function before nextPrime function

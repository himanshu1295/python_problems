# Given an integer N find the sum of the first N natural number.

def nSum():
    n = int(input("Enter a number: "))
    
    ans = 0
    ans = n * (n + 1) // 2  # return int data type instead of float

    print(ans)

nSum() 

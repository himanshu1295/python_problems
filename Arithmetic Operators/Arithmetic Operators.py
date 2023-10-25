# Arithmetic Operators Problem :

# You are given two integer variables x and y. You need to perform the following operations:

# p = x+y : Addition
# q = x-y : Subtraction
# r = x*y :Multiplication
# s = x/y : Float Division with a precision of 5 decimal places
# t = x//y : Int Division
# u = x%y : Modulous
# v = x**y : Power

x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))

class Solution:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operation(self):
        p = self.x + self.y
        q = self.x - self.y
        r = self.x * self.y
        s = round(self.x / self.y,5)
        t = self.x // self.y
        u = self.x % self.y
        v = self.x ** self.y
        print("Addition :", p)
        print("Subtraction :", q)
        print("Multiplication :", r)
        print("Float Division :", s)
        print("Int Division :", t)
        print("Modulus :", u)
        print("Power :", v)

solution_instance = Solution(x, y)
solution_instance.operation()
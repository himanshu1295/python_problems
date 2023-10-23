# write a program to print table of a given number

n = int(input("Enter a number: "))

for i in range(1, 11):
    table = n * i
    print("{} * {} = {}".format(n, i, table))


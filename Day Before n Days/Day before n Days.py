# Problem : Day before n Days

# d = day which starts from Sunday which is 0

# 0 means Sunday, 1 means Monday, 2 means Tuesday, 3 means Wednesday, 4 means Thursday 
# 5 means Friday, 6 means Saturday

d = int(input("Enter d: "))
n = int(input("Enter the number of days: ")) # Enter the number of days you want to know the date before

result = (d - n) % 7

print()

print("Day is :", result)

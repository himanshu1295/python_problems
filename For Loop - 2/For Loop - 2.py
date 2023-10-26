# You are given a String s, you need to print its characters at even indices(index starts at 0).

def even_index():
    s = input("Enter a string: ")

    for i in range(0, len(s), 2):
        print(s[i], end = " ")

even_index()

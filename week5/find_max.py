def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    print('This line will never be executed')

print(find_max(10, 20))
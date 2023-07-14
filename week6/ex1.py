def print_line(n, symbol):
    for i in range(n):
        print(symbol, end="")
    

def print_normal_triangle(n):
    for i in range(1, n + 1):
        print_line(i, '# ')
        print()

def print_reverse_triangle(n):
    for i in range(1, n + 1):
        print_line(n - i, '  ')
        print_line(i, '* ')
        print()

def print_bottom_triangle(n):
    for i in range(n, 0, -1):
        print_line(i, '* ')
        print()

def print_triangle(n, mode):
    if mode not in ['normal', 'reverse', 'bottom']:
        print("Invalid mode")
        return

    if mode == 'normal':
        print_normal_triangle(n)
    elif mode == 'reverse':
        print_reverse_triangle(n)
    else:
        print_bottom_triangle(n)


mode = input('Enter mode: ')
n = int(input('Enter number of line: '))
print_triangle(n, mode)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_primes(n, m):
    count = 0
    for p in range(2, n + 1):
        if is_prime(p):
            count += 1
            print(p, end=' ')
            if count == m:
                print()
                count = 0

n = int(input('Enter n: '))
print_primes(n, 5)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input())
prime_numbers = [str(num) for num in range(2, limit + 1) if is_prime(num)]
print(' '.join(prime_numbers))
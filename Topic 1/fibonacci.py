def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
limit = 10
fib_sequence = [str(fibonacci(i)) for i in range(limit)]
print(f"Fibonacci sequence up to {limit} numbers:", ' '.join(fib_sequence))
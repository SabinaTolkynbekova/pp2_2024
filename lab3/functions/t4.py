def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    """Filter prime numbers from the list."""
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

numbers_input = input("Numbers: ").split()
numbers_list = list(map(int, numbers_input))

prime_numbers = filter_prime(numbers_list)
print(prime_numbers)

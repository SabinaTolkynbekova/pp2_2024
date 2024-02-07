def is_prime(n):
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

numbers = [23, 45, 12, 67, 89, 2, 3, 5, 7, 11, 13, 17]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers) 
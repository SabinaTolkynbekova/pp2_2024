def calculate_factorial(n):
    if n==0:
        return 1
    else:
        return n * calculate_factorial(n-1)

number = int(input())
if number < 0:
    print("Factoorial is not defined")
else:
    print(calculate_factorial(number))
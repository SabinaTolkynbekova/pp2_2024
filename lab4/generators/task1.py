def squares_generator(n):
    for num in range(n,n+1):
        yield num**2

n = int(input())
squares = squares_generator(n)
for square in squares:
    print(square)


    
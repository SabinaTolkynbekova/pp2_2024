def squaress(a,b):
    for num in range(a,b+1):
        yield num**2

a = 2 
b = 8

for square in squaress(a,b):
    print(square)

#another way of solving
def squaress(a,b):
    square = (i**2 for i in range(a,b+1))
    for i in square:
        print(i)

a = int(input())
b = int(input())
squaress(a,b)
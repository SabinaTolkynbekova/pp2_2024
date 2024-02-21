def generator(n):
    for num in range(n+1):
        if num%3==0 and num%4==0:
            yield num

n = int(input())
d = generator(n)
for num in d:
    print(num)
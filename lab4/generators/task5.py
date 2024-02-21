def down_to_zero(n):
    while(n>0):
        n-=1
        yield n

n = int(input())
for i in down_to_zero(n):
    print(i)
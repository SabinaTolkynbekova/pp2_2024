import math
side = int(input())
length = int(input())
area = side*length**2/(math.tan(math.pi/side)*4)
print(area)
import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    
    def move(self, x2, y2):
        self.x = x2
        self.y = y2

    def dist(self, other_point):
        distance = math.sqrt((self.x-other_point.x)**2 + (self.y - other_point.y)**2)
        return(distance)
    
a = int(input())
b = int(input())
c = int(input())
d = int(input())

point1 = Point(a,b)
point2 = Point(c,d)
        
point1.show()
point2.show()

e=int(input())
f=int(input())
point1.move(e,f)
point1.show()

distance= point1.dist(point2)
print("distance: ", distance)



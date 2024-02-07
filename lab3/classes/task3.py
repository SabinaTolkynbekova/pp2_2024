class Shape:
    def __init__(self):
        pass

    def area(self): 
        return 0

class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__()
        self.length = length
        self.width = width
    

    def area(self):
        return self.length*self.width

a=int(input())
b = int(input()) 
s = Rectangle(a, b)

print(s.area())
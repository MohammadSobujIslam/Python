class Shape():
    def __init__(self,length,height):
        self.length=length
        self.height=height
    def area(self):
        print('I calculate shape class area')    


class Triangle(Shape):
    def area(self):
        result=self.length*self.height*0.5
        print(f"Triangle area = {result}")



class Rectangle(Shape):
    def area(self):
        result=self.length*self.height
        print(f"Triangle area = {result}")



t=Triangle(3,6)
t.area()
r=Rectangle(4,5)
r.area()        
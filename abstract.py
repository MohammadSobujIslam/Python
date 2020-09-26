from abc import ABC ,abstractmethod
class Shape(ABC):
    def __init__(self,length,height):
        self.length=length
        self.height=height
    @abstractmethod
    def area(self):
    
       pass   


class Triangle(Shape):
    def area(self):
        result=self.length*self.height*0.5
        print(f"Triangle area = {result}")



class Rectangle(Shape):
    def area(self):
        result=self.length*self.height
        print(f"Triangle area = {result}")


#s=Shape(4,6) abstract class naver call
t=Triangle(3,6)
t2=Triangle(10,10)
t2.area()
t.area()
r=Rectangle(4,5)
r.area()        
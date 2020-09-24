class triangle:
   
    def __init__(self,base,height):
        self.base=base
        self.height=height
       
       

    def areacal(self):
        area=0.5*self.base*self.height; 
        print(f"Triangle area = {area}")
    
      
class area(triangle):
    def __init__(self, length, h,base,height):
        super().__init__(base,height)
        self.length=length
        self.height=h
        area=self.length*self.height
        print(area)

       



t1=triangle(4,10)
t1.areacal()

t2=area(5,7,4,6)









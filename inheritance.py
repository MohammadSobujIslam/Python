class person:
    def __init__(self,fname,lname):
        self.first_name=fname
        self.last_name=lname
    def diplayPerson(self):
        print(f"Full name: {self.first_name} {self.last_name}") 
        


p=person('mohammad','sobuj')
p.diplayPerson()

class Student(person):
    def __init__(self, fname, lname,year,age):
        super().__init__(fname, lname)
        #self.year=2020
        self.year=year
        self.age=age
    #pass

s=Student('junayed','hasan',2020,22)
s.diplayPerson()
print(s.year)
print(s.age)
s.diplayPerson()

class child(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname, lname)
        self.person_name='person name is Nazmul hasan'


c=child('tafsan','hasan')
s=child('mostakim','islam')
c.diplayPerson()
print(c.person_name)
s.diplayPerson()

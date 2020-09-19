print(2)
def my_function():
    print("hello function")


my_function()
def name_display(first_name,last_name):
    print("Hi "+first_name+" "+last_name)


name_display('mohammad','sobuj') 
name_display('mis','afsana akter')
def number_square(number):
    result=number**2
    print(result)  

number_square(3)  

def number_add(number1,number2,number3):
    
    return number1+number2+number3

result=number_add(2,46,6)
print(result)   

def f_tuple(*kids):
    print("your tuple value " + kids[-2])

f_tuple('email','tobias','lonus')    

def my_functional(child3, child2, child1):
      print("The youngest child is " + child1)

my_functional(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_functionalyty(**child):
      print("The youngest child is " +child['child2'] )

my_functionalyty(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
def my_function(food):
      for x in food:
          print(x)

#fruits = ["apple", "banana", "cherry"]

my_function(["apple", "banana", "cherry"])
def myfunction():
  pass
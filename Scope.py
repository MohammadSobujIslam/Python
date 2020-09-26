

x='Scope'# Global Scope
def Scope():
    x=100
    print(x)
    def innerfun():
        x=200
        print(x)
    innerfun()
    print(x)     # Local Scope


Scope()
print(x)

def Scope1():
    #x=100
    print(x)
    def innerfun():
        #global x
        #x=499
        print(x)
    innerfun()
    print(x)     # Local Scope


Scope1()
print(x)

def Scope2():
    global x
    x=5000
    print(x)
    def innerfun():
        x=200
        print(x)
    innerfun()
    print(x)     # Local Scope


Scope2()
print(x)

import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%D"))
print(x.strftime("%Y"))
print(x.strftime("%X"))
print(x.strftime("%T"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%Z"))
print(x.strftime("%%"))
a=datetime.datetime(2020,4,5)
print(a)
print(a.strftime("%B"))

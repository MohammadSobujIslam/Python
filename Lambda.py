a=lambda s:s+10
b=a(20)
print(b)
result=(lambda s:s**2)(20)
print(result)
def Multiple(n):
    return lambda a:a*n

resalt=Multiple(5)
#re_resalt=resalt(5)
print(resalt(20))
print(type(resalt))
print(resalt(200))
def add(num1,num2):
    add=num1+num2
    sub=num1-num2
    return add+sub
callb=lambda a,b,c:a*b+c
r=add(4,5)
print(r )
print(callb(2,3,4))



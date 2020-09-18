print()
tupl1=('sobuj','jihad','junayed','tafsan','mostaque')
print(tupl1)
print()

print(tupl1.index('sobuj'))
print(tupl1[1])
print(tupl1[-1])
x=list(tupl1)
x.append(1)
x.insert(0,44)
tupl=tuple(x)
print(x)
print(tupl)
for item in tupl:
    print(item)
if 'sobuj' in tupl:
    print("existent in tupl valur")    
else:
    print("No existent")
length=len(tupl)
print(length)
print(type(tupl))
#del tupl fully delete in tuple 
print(tupl)
tupl2=tupl+tupl1
print(tupl2)
tupl3=tuple(tupl1)
tupl3=tuple(tupl)
print(tupl3)
# unpacking tuple or list
# first unpack in tuple
tuple_unpack=(11,2,4,4)
result=tuple_unpack[0]*tuple_unpack[1]*tuple_unpack[2]
x=tuple_unpack[0]
y=tuple_unpack[1]
z=tuple_unpack[2]
print(tuple_unpack)
print(result)
print(x)
(a,b,c,d)=tuple_unpack
print(b)
# unpack in list

list_line=[3,6,7]
(m,n,o)=list_line
print(m)


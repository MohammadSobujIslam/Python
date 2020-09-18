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

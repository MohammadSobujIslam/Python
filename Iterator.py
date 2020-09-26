Mytuple=('apple','banana','cherry')
myitar=iter(Mytuple)
print(myitar)
print(next(myitar))
print(next(myitar))
print(next(myitar))

strings="python for beginner"
itar=iter(strings)
'''
print(next(itar));
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))
print(next(itar))

for ins in strings:
    print(ins)

class MyNumbers:
    def __iter__(self):
         self.a = 0
         return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
class MyNumbers:
    def __iter__(self):
         self.a = 0
         return self

    def __next__(self):
        if self.a<=20:
           x = self.a
           self.a += 1
           return x
        else:
            raise StopIteration   

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)

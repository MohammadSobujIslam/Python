''''
value=int(input("Enter your number:"))
for i in range(0,value):
    print(" "*(value-i-1)+"* "*(i+1))

for j in range(value-1,0,-1):
    print(" "*(value-j)+"* "*(j))
'''

a=int(input("Enter your number:"))
for i in range(1,a+1):

    for j in range(1,a+1):
        print(i,end='') 
    print()
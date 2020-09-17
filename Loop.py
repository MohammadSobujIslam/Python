# Today I learn loop
# First in While loop
""""
i=10

while i>=1:
    print(f"{'*' * i } {' '*i} {'*'*i} ")


    #print(f'next iteration {i}')
    i-=1

print("Done")
i=10

j=1

while j<=10:
    print('*'*j)
    #print(f'next iteration {i}')
    j+=1

print("Done")

#number=int(input("Guess"))
win_number=9
gues_count=0
gues_limit=3
while gues_count<gues_limit:
    gues=int(input("gues: "))
    gues_count+=1
    if  win_number==gues:
        print('Winners!')
        break
else:
    print('Sorry, you Failed! ')
    print("Again Try")

ca=4.7
print(type(ca))
for item in "python for sobuj":
    print(item)
print("Done")

list=[1,4,'sobuj','mosh',[1,3,7,6,5,4]]
for list in list:
    print(list)

print("list done")
"""
for i in range(1,20,10):
    if i%2==1:
        print(i)
    #else:
        #print(i)
print("print all odd number")
var=3j
print(var)
for x in range(3):
    for y  in  range(4):
        print(f"({x},{y})")




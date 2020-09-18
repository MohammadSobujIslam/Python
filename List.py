
# List are same array in javascript
name=['sobuj','shohag','razib','shanto','jihad','junayed']
print(name)
print(name[2:4])
print(name[:])
print(name[:3])
print(name[0][:3])
number_list=[111,4,2,7,2,88,77]
max = number_list[0]
min=number_list[0]
for i in number_list:
    if i>max:
        max=i
print(max)    

for j in number_list:
    if j<min:
        min=j
print(min) 

# 2D list 
list2=[1,3,'sobuj',4,'tafsan',5,number_list,3,[1,4,6,7]]
print(list2)
list3=[
    [2,4,5],
    [3,4,4],
    [5,0,6]
]
print(list3)
print(list3[2][2])
for i in list3:
    print(i)

for j in list3:
    for k in j:
        print(k)

"""
number=int(input("enter your number ")) 
flag=-1
list=[]
for i in range(2,number):
    if number%i==0:
        flag=1;
        break
    
if flag==-1:
    print(f" {number} number is prime ")

else:
     print(f"{number} number is not prime ")

list_number=[1,1,3,2,5,9]

list_number.append(4)
list_number.insert(1,9)
list_number.insert(5,9)
list_number.insert(0,33)
print(list_number)
print(list_number.count(9))
print(list_number.count(1))
list_number.sort()
print(list_number)
list_number.reverse()
print(list_number)
list_copy=list_number.copy()
print(list_copy)
list_copy.append(2000)
print(list_copy)

list_number.remove(9)
list_number.append(100)

#list_number.clear()
#list_number.pop()
print(list_number)
print(list_number.index(100))
#print(list_number.index(1001))
print(101 in list_number)
"""

list_number=[1,1,3,2,2,5,9,6,6]
unique=[]
for same in list_number:
    if same not in unique:
        unique.append(i)
print(unique) 
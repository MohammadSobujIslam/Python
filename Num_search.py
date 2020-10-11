import numpy as np
'''
arr=np.array([1,3,5,6,7,8,9])
x=np.where(arr==4)
print(x)
y=np.where(arr%2==1)
print(y)
s=np.searchsorted(arr,54)
print(s)
sr=np.searchsorted(arr,5,side='right')
print(sr)
mltp=s=np.searchsorted(arr,[1,3,4])
print(mltp)
search=np.searchsorted(arr,6)
print(search)

# Numpy array sort 
arr=np.array([3,1,7,40,4,8,11,1])
srt=np.sort(arr)
print(srt)
print(arr)
arr_bool=np.array([True,False,False])
print(np.sort(arr_bool))
'''

# Filtering in Numpy array

arr = np.array([41, 42, 43, 44])

x = [True, False, False,True]

newarr = arr[x]

print(newarr)
filter_arr=[]
for fil in arr:

    if fil >42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)    
newarr=arr[filter_arr]
print(newarr)
print(filter_arr)

arr1=np.array([3,1,7,40,4,8,11,1])
filter_arr1=[]
for fil in arr1:
    if fil%2==0:
        filter_arr1.append(True)

    else:
        filter_arr1.append(False)

newarr1=arr1[filter_arr1]
print(newarr1)

filter_ar=arr1>4
narr=arr1[filter_ar]
print(narr)

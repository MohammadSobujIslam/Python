import  numpy
#
'''
arr=numpy.array([2,4,566,7])
print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.ndim)
arr=np.array([1,3,5,67,88,89,9],ndmin=6)
print(arr)
print(arr.shape)
print(np.__version__)
print(np.__version__)
print(numpy.__version__)
print(type(arr))
arr=np.array(2)
print(arr)
arr=np.array([[1,2,3,4,5,6],[2,4,6,6,7,3],[3,5,6,7,1,4]],dtype=complex)

print(arr)
arr=np.array([[1,2,3,4,5,6],[2,4,6,6,7,3],[3,5,6,7,1,4]])
print(arr)
print(arr.ndim)
print(arr.shape)
arr=np.dtype(np.int32)
arr=np.dtype('>i4')
arr=np.arange(34)

print(arr)
arr=np.array([1,2,3,4,5,6,9,6,4])
print(arr[::2])

arr=np.array([[[1,2,3,4,5,6],[1,4,6,8,99,3]],[[2,4,6,6,7,3],[1,4,6,77,99,3]],[[3,5,6,7,1,4],[1,4,6,7,89,3]]])
print(arr)
print(arr.ndim)
print(arr.shape)
#arr=np.arange(24).reshape(2,3,2,2)
print(arr)
print(arr[1,1,])
print(arr[1,0,0:3])
print(arr[1,0:4,0:3])

arr =np.array([[6, 7, 8,3, 9,3,10,6,8],[1,3,45,4,6,667,5,7,1]])
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(type(arr))
print(arr[1,1:8:2])

arr=arr.reshape(3,6)
print(arr)
print(arr.ndim)
arr=np.array([2,4,5],ndmin=8,dtype=complex)
print(arr)
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

arr=np.array([1.3,4.3,4.1,5.6,44,6,6.3])
x=arr.copy()
x[3]=100

arr[2]=200
print(arr)
print(x)

arr=np.array([1,4,6,78,7,8,9,90,7,8])
v=arr.view()
c=arr.copy()
v[0]=100
arr[1]=777
print(arr)
print(v)
print(v.base)
print(c.base)
print(arr.shape)
arr=np.array([[1,4,6,78,7,8,9,90,7,8],[1,4,6,78,7,8,9,90,7,8]])
print(arr.shape)
arr=np.array([[1,4,6,78,7,8,9,90,7,8],[1,4,6,78,7,8,9,90,7,8]],ndmin=6)
for i in arr:
    print(i)
print(arr)
print(arr.shape)
'''
'''
arr=np.array([1,4,6,7,8,9,90,7,3,2,4,5,1,2,3,4])
rs=arr.reshape(2,2,4,-1)
#print(rs)
print(rs.shape)
r=rs.reshape(-1)
print(r)
print(rs.reshape)
for i in r:
    #print(i)
    pass

arr=np.array([[[1,4,6,78,7,8,9,90,7,8],[1,4,6,78,7,8,9,90,7,8]],[[1,4,6,78,7,8,9,90,7,8],[1,4,6,78,7,8,9,90,7,8]]])
for i in arr:
      
    for j in i:
        
        for k in j:
            #print(k)
            pass


for i in np.nditer(arr):
    #print(i)
    pass
arr=np.array([1,3,5,6,7,88,31,44])
for i in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    #print(i)
    pass
arr1=np.array([[1,3,5,5,2],[4,3,5,6,7]])
for i in np.nditer(arr1[:,:4:2]):
    #print(i)
    pass
for ind,i in np.ndenumerate(arr1):
    #print(ind,i)
    pass
arr2=np.array([1,3,5,67,88,99,546])
arr1=np.array([2,4,54,6,54]) 
for idx,i in np.ndenumerate(arr2):
    print(idx,i)   
add_arr=np.concatenate((arr1,arr2))
print(add_arr)
ar2=np.array([[1,2],[3,4]])
ar3=np.array([[11,22],[33,44]])
add_2ar=np.concatenate((ar2,ar3), axis=1)
print(add_2ar)
add_2ar=np.concatenate((ar2,ar3), axis=0)
print(add_2ar)
'''
'''
ar1=np.array([1,3,5,6])
ar2=np.array([3,7,0,0])
arr_add=np.stack((ar1,ar2),axis=1)
arr_add_row=np.hstack((ar1,ar2))
arr_add_col=np.vstack((ar1,ar2))
arr_dd=np.dstack((ar1,ar2))
print(arr_add)
print(arr_add_row)
print(arr_add_col)
print(arr_dd)
'''
'''
arr=np.array([1,3,5,6,6,7,77,8,754,4,54,4,7,5,8,8,2,1,6])
new_arr=np.array_split(arr,4)
print(new_arr)
print(new_arr[0])
print(new_arr[3])

arr=np.array([[1,3,5,6],[6,7,77,8],[754,4,54,4],[7,5,8,8],[2,1,6,8]])
new_arr=np.array_split(arr,3)
print(new_arr)
new_arr=np.array_split(arr,5,axis=1)
print(new_arr)
#print(new_arr[0])
print()
#print( new_arr[3])

#arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr,3)
vs = np.vsplit(arr,3)
#ds= np.dsplit(arr,3)


print(newarr)
print(vs)
st=np.hstack(arr)
vv=st=np.vstack(arr)
#d=st=np.dstack(arr)
print(st)
print(vv)
'''

from numpy import random

x = random.randint(100)

print(x)

x = random.rand()

print(x)
x = random.randint(100,size=(5))

print(x)
   











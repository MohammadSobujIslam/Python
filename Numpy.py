import numpy
import numpy as np
'''
arr=numpy.array([1,3,5,6,7,8,91,143,144,4])
#print(arr)
arr1=['sobuj','java','javascript','python','c',2,3,4,1]
ar=numpy.array(arr1)
#print(ar)
ar1=np.array(arr1)
print(ar1)
print(np.__version__)
arr2=np.array([1,2,3,4,5])
print(arr2)
print(type(arr2))
arr3=np.array((1,4,6,8))
print(arr3)
print(type(arr3))
ob=np.array({'name':'sobuj','1':'one','np':'numpy'})
print(ob)
print(type(ob))
arr_0=np.array(00)
print(arr_0)
print(type(arr_0))
arr_towd=np.array([[1,2,3],[1,4,6],[2,3,5]])
#print(arr_towd)
arr_3d=np.array([[[12,3,5],[33,2,1],[43,3,0]],[[1,1,2],[4,4,5],[55,5,6]]])
print(arr_3d)
print(arr_0.ndim)
print(arr2.ndim)
print(arr_towd.ndim)
print(arr_3d.ndim)
arr_di=np.array([1,2,3,4],ndmin=6)
print(arr_di)
print('Dimenssion in array arr_di:',arr_di.ndim)


arr_r=np.array([1,2,3,4,6])
print(arr_r)
print(arr_r.ndim)
print(arr_r[1])
print(arr_r[-4:-1])
print(arr_r[3]+arr_r[4])
arr_2dr=np.array([[1,3,5],[4,5,6],[1,1,9],[0,9,0]])
print(arr_2dr[[0]])
print(arr_2dr[[2]])
print(arr_2dr[1,2])
print(arr_2dr[3,2])
arr_3=np.array([[[1,2,3], [2,3,5]], [[1,1,1],[2,3,4]], [[1,34,5,],[3,5,7]]])
print(arr_3)
print(arr_3.ndim)


arrthree= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arrthree)
print(arrthree[0,0,1])
print(arrthree[1,0,1])
print(arrthree[-1,0,-1])
ar=np.array([1,2,3,4,5,6,7,8,9,10,11,12,12,13,14])
print(ar[1:5:2])
print(ar[3:14:3])
arr_2d=np.array([[1,3,5,8,9,3,1],[1,1,1,2,4,5,6],[3,4,6,8,1,1,9],[3,2,4,6,0,9,0]])

print(arr_2d[1, 1:3])
print(arr_2d[0:4,1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# Numpy data type
arrr=np.array([1,2,3,4,5,6,7,8,9,0])
print(arrr.dtype)
aar=np.array([1,2,3,4])
print(aar.dtype)
arr = np.array([1, 2, 3, 4])

print(arr.dtype)
arr=np.array(['apple','banana','cherry'])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
arr = np.array([7, 2, 3], dtype='i')
print(arr)
print(arr.dtype)
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()

arr[0] = 42

print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
# Numpy =Numerical python

print(x.base)
print(y.base)
print(arr.base)
nw= arr.astype(int)
print(nw)
print(nw.dtype)
c=arr.copy()
v=arr.view()
print(c)
print(v)
v[0]=100
c[1]=400
print(c)
print(v)
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
arr=np.array([[1,3,4,5,6],[2,78,22,4,6]])
print(arr.shape)
print(arr.shape)
ara=np.array([1,2,3,4], ndmin=5)
print(ara)
print(ara.shape)
arr=np.array([[[1,2,3],[2,4,6],[2,1,3],[5,7,8]],[[5,6,8,],[1,2,4],[23,5,6],[5,9,0]]])
print(arr)
print(arr.shape)
arr = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
print(newarr.shape)

'''
arr=np.array([2,4,6,8,10],ndmin=2)
print(arr)
print(arr.shape)
print(arr.dtype)
arr=np.array([2,4,6,8,10],ndmin=5)
print(arr)
print(arr.shape)
arr=np.array([[1,3,5,5],[1,3,5,5],[1,3,5,5],['ao','e','b','r']])
print(arr)
print(arr.shape)
print(np.__version__)
print(arr.shape)
print(type(arr))
arr=np.array(43)
print(arr)
print(type(arr))
print(arr.shape)
arr_1d=np.array([1,2,3,4])
print(arr_1d)
print(type(arr_1d))
print(arr_1d.shape)
print(arr_1d.dtype)

ar_2d=np.array([[1,3],[2,5]])
print(ar_2d)
print(ar_2d.ndim)
list_arr=[[1,6,4,4],
[3,5,67,77,8,8],
[84,6,7]
]
print(list_arr)
# finally i can understand list are array object(ndarray) not same(list!=ndarray)
ar_3d=np.array([[[3,4,5],[3,4,5]]])
print(ar_3d)
print(ar_3d.shape)
print(ar_3d.ndim)
ar_higher=np.array([3],ndmin=6)
print(ar_higher)
print(ar_higher.ndim)
a=ar_higher[:]
print(a,8)
arr=np.array([1,2,3,4,5,6])

print(arr[0])
print(arr[-4:-1])
print(arr[0]+arr[3])
ar_2d=np.array([[1,3,4,6,7,17,8,8],[3,5,78,7,99,99,2,5]])

print(ar_2d[1,5])
print(ar_2d.size)
print(ar_2d.shape)
arr=np.array([[[1,2,3],[2,4,6],[2,1,3],[5,7,8]],[[5,6,8,],[1,2,4],[23,5,6],[5,9,0]]])
print(arr.shape)
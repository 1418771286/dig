import numpy as np

d3 = np.arange(2, 45, 3).reshape(5,3)
d3 = np.mat(d3)
print(d3)
print(type(d3))
d1 = np.arange(20).reshape(4, 5)
print(d1)
print(type(d1))
d13 = d1 * d3
print(d13)
print(type(d13))
a = np.array([[1, 2], [3, 4], [4, 1]])
print(a)
print(a.shape)
print(a.ndim)
import numpy as np
a = np.array([[5, 9], [3, 7], [8, 6]])
b=np.sort(a,axis=0)
print(b)
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.resize(a,(3,4))   #将数组a调整为3行4列的新数组b
print(b[1,2])
print("!")
a = np.arange(20).reshape(4,5)
print(a)
print(a[1,3])
print(a[2,:])
print("?")
b = np.reshape(a,(5,4))
print(b)

import numpy as np

""" 
a=np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)
"""

'''
b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])
'''

'''
a=np.zeros((2,2))
print(a)

b=np.ones((1,2))
print(b)

c=np.full((2,2),7)
print(c)

d=np.eye(2)
print(d)

e=np.random.random((2,2))
print(e)
'''

'''
a=np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a[0,1])

# first 2 rows and columns 1 and 2
b=a[:2,1:3]
print(b)

# modify the original array
b[0,0]=100
print(a)
'''

'''
# Mixing integer indexing with slices yields an array of lower rank
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row1=a[1,:]
row2=a[1:2,:]
print(row1)
print(row2)

col1=a[:,1]
col2=a[:,1:2]
print(col1)
print(col2)
'''

'''
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b=np.array([0,2,0,1])
print(a[np.arange(4),b])
a[np.arange(4),b]+=10
print(a)
'''

'''
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx=(a>2)
print(bool_idx)
print(a[bool_idx])
print(a[a>2])
'''

'''
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x+y)
print(np.add(x,y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))
'''

'''
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
'''

'''
x = np.array([[1,2],[3,4]])

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
'''

'''
x=np.array([[1,2],[3,4]])
print(x)
print(x.T)

# taking the transpose of a rank 1 array does nothing
y=np.array([1,2,3])
print(y)
print(y.T)
'''

'''
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) 

for i in range(4):
    y[i,:]=x[i,:]+v

print(y)
'''

'''
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print(y)

'''

'''
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 2)) 
print(v)
print(vv)
'''
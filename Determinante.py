import numpy as np

A = np.array ([[1,2,4],[5,3,-1],[7,2,0]])

print(A)

det_A = np.linalg.det(A)
print(det_A)

#print (help(np.linalg.det))

a = np.array([[1, 2], [3, 4]])
det_a = np.linalg.det(a)
print(det_a)


#posso também importar todo o caminho
from numpy.linalg import det

print(det(A))

B = np.array([[1,2,4,5,6,7], [5,3,-1,5,1,2],[7,2,0,1,4,9]])
print(B)

print(B.shape)

print(det(B))

print(array)

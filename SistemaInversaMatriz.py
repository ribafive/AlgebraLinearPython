import numpy as np
from numpy.linalg import det,  inv

A = np.array([[-1,2],[2,1]])
B = np.array([[-1],[5]])

print (det(A))
print (A)
print (B)

#vetor solução
print(inv(A),"\n\n")
X = inv(A).dot(B)
print(X)

#Sistema 3x3
G = np.array([[1,2,3],[6,0,1],[4,5,-1]])
H = np.array([[3],[-6],[1]])
print(G,"\n\n")
print(H,"\n\n")

print(det(G))
s = inv(G).dot(H)
print (s)
print(G.dot(s))

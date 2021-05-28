import numpy as np
from numpy.linalg import det

A = np.array ([[1,2,4],[5,3,-1],[7,2,0]])
Az = np.zeros ([3,3])

print(A)
print(Az)

#Propriedades

#1 - det(Az) = 0

print (det(Az))

#2- det(A) = det(A.T)
print(det(A))
print(det(A.T))

#3- Se B = K * A[0,:], det(B) = K * det(A)
K = 3
B = A.copy()
B[0,:] = K * B [0,:]
print(B)
print(det(B))
print(det(A))
print(K * det(A))

#4- Se trocarmos de duas linhas o determinante muda de sinal
L1 = A[0,:] #Linhas 1
L2 = A[1,:] #Linhas 2
L3 = A[2,:] #Linhas 3

C = np.array ([L2,L1,L3])
print(C)
print(det(C))
print(det(A))

#5- Matriz com duas linhas iguais  -> det = 0
D = np.array ([L1,L1,L3])
print(D)
print(det(D))

#6- det(A+B) != (det(A) + det(B))
A = np.array([[1,2,4],[5,3,-1],[7,2,0]])
B = np.array([[0,5,4],[8,2,1],[9,-2,3]])

print(np.array_equal(det(A+B),det(A)+det(B)))
print(det(A+B))
print(det(A)+ det(B))

#7- det(A.dot(B)) = det(A)*det(b)
print(det(A.dot(B)))
print(det(A)*det(B))

import numpy as np
from numpy.linalg import det,  inv

A = np.array([[1,-7,2],[4,2,7],[1,4,-1]])
B = np.array([[1,1,2],[1,1,2],[3,-1,-1]])
C = np.array([[1,3,2],[1,5,2],[4,-1,-1]])

print (A)
print (B) #Quando matriz tem duas linhas iguais o determinate é zero

print(det(A))#Se determinante for != 0 existe a matriz inversa
print(det(B))


inv_A = inv(A)

print(inv_A)#Matriz inversa

print(A.dot(inv_A))#Matriz identidade

print(det(C))

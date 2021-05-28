import numpy as np
from numpy.linalg import det,  inv

# OBS: Sabemos que essas matrizes não representam casos gerais!

A = np.array([[1,-2,3],[4,6,1],[0,2,1]])
B = np.array([[0,2,5],[1,3,1],[0,1,-3]])

print(A,"\n")
print(B,"\n")

print(det(A))
print(det(B))

#1) Caso A possua inversa de A^-1, a inversa de A^-1 também existe
print(inv(A))
print (inv(inv(A)))

#2)Caso A e B possuirem inversas, então AB também possui inversa: (A*B)^-1 = B^-1*A^-1
print(np.array_equal(inv(A.dot(B)), inv(B).dot(inv(A)))) #Atenção, quando a dizima é mto grande a função equal não funciona tão bem
print(inv(A.dot(B)),"\n")
print (inv(B).dot(inv(A)),"\n\n\n") #As duas são iguais, validando a propriedade

#3) A Inversa de A.T é igual a inversa(A).T
print(A,"\n")
print(inv(A.T),"\n")
print(inv(A).T)

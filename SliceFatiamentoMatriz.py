import numpy as np

A = np.array ([[2,4,6] , [4,7,1] , [9,3,8]])

print (A, "\n")
print (A.shape, "\n\n")

#Slicing
print (A[:],"\n")
print (A[:,:],"\n\n") #pegando toda linha e toda coluna

#se eu quiser pegar todos os elementos da segunda linha
print (A[1,:]) #Lembrando que a primeira linha começa com indice 0

print (A[2, :])


#pegar um elemento especifico
print (A[1,1])


B = A #Não estou copiando e sim refenciando
B[1,2] = 77
print (B)
print (A) #Por conta da referencia a matriz A também foi mudada.



#Cópia de matrizes
C = B.copy()
print (C)

C[2,0] = 123
print (C)
print (B)

F = C[:,1].copy()

print(F)




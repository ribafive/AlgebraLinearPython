import numpy as np

A = np.array ([[2,4,6],[1,2,7],[3,2,9]])
B = np.array ([[-1,4,5],[6,3,1]])
C = np.array ([[0,4,3],[1,-3,-1],[3,1,2]])

print (A)
print ("\t\t\t",A.shape,"\n\n")

print (B)
print ("\t\t\t",B.shape,"\n\n")

print (C)
print ("\t\t\t",C.shape,"\n\n")

#Soma - Atenção

SL = A[0,:] + B[0,:]
print (SL)

S = A + C
print (S)

#Subtração

Sub = A - C
print (Sub)


#Multiplicação

M = A * C
print (M)

#Divisão

D = A / C
print (D)

#Multiplicação por escalar
k = 2
print(k * A)

#Multiplicação matricial
MS = A.dot(C)
print(MS)
#Validando multiplicação
MS11 = A[0,:].dot(C[:,0])
print(MS11)
MS12 = A[0,:].dot(C[:,1])
print(MS12)
MS13 = A[0,:].dot(C[:,2])
print(MS13)


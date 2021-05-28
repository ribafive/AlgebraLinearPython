import numpy as np

A = np.array ([[2,3,7,1],[8,6,9,3],[6,9,3,2],[4,3,7,5]])

print (A.shape)

print (A, "\n\n")

#print(A[2,1:3],"\n\n") #o último item não é inclusivo

#print(A[3,0:3])

print(A[1:4,2])

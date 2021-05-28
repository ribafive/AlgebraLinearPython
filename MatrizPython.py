import numpy as np

#Matriz

A = np.array ([[2,1],[0,4]])

print ((A),"\n\n")


#Matriz 2 x 3

B = np.array ([[1,0,4],[4,-3,2]])

print ((B),"\n\n")

print (type(B),"\n\n")



#Matriz 2 representação

help (np.matrix)
#F = np.matrix()

a = np.matrix("1 2; 3 4")
print (a)

D = np.matrix ([[2, -1],[0,4]])
print (D)

print (type(D))

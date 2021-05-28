import numpy as np

#Matriz Linha
L = np.array ([3,4,5])

print (L)

L2 = np.array ([[2,3,4]]) #aqui tem uma lina e tres colunas

print (L2)

print (L.shape)
print (L2.shape) #aqui tem uma lina e tres colunas


#Matriz Coluna

C1= np.array([[1],[2],[3]])

print (C1)
print (C1.shape) # 3 linhas e uma coluna

#Matriz Nula

N = np.zeros([2,2])
print (N)

N3 = np.zeros([5,5])
print (N3)

#Matriz Diagonal

D = np.diag([1,3,7,8,4])
print (D)
print (D.shape)

#Matriz Identidade

I = np.eye(4,4)
print (I)

## print(help(np.eye))

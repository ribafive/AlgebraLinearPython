import numpy as np

S = np.array ([[1,4,3], [4,2,5], [3,5,0]])
A = np.array ([[1,2,3,6], [9,7,4,6]])
B = np.array ([[8,5,3,3], [1,0,1,8]])

print (S,"\n")

print (np.transpose(S),"\n\n") #Igual ela mesma pois ela é simétrica

print(A, "\n")
print(np.transpose(A),"\n\n")

print(A.T,"\n\n") #atalho para transpose (ou matriz transposta)

#Função que compara a igualadade de duas matrizes
print (np.array_equal(S,S.T))



##Provando a segunda propriedade
# A" = A

print(np.array_equal(A.T.T, A))


##Terceira propriedade
# (A + B)' = A' + B'

print (np.array_equal((A + B).T, A.T + B.T))

##Quarta Propriedade
# (KA)' = KA' ; onde K é qualquer escalar

K = 7
print(np.array_equal((K*A).T, K*A.T))

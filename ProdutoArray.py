import numpy as np

u = np.array ([2,3])

v = np.array ([4, -1])

#Produto de elementos dos vetores
print ("\n\nProduto ou multiplicação de vetores:\n",v * u,"\n")

#Produto interno ou produto escalar
print ("Produto escalar de U e V:\n",u.dot(v),"\n")

print("\tMódulo: Pega o vetor e faz o produto interno ou produto escalar dele por ele mesmo e tira a raiz\n")
#Módulo
mod_u = np.linalg.norm(u)
print ("O módulo de U é: \n",mod_u,"\n")

#O que ela faz? Pega o vetor, faz o produto interno e tira a raiz
print ("Módulo de V é: \n",np.linalg.norm(v))

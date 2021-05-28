import numpy as np

#Corrida Uber

p = 1.2 #Preço Km
x = 0 #Km

C = p * x

print (C)

#Netflix

v = np.array([0.3, 0.4, 0.8, 0.1, 0.7]) #espaço vetorial 5 dimensões
c = 40
a = 10
d = 20
t = 10
s = 90
x = np.array([c, a, d, t, s])

Q = v.dot(x) #multiplicação de matrizes
print(Q) #Número de pessoas

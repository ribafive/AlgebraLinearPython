import numpy as np

u = [1,2,9]
v = [2,1,4]



count = len(u) 
print ("contador", count)
vetor = []

for n in range (count):
    vetor.append  ((u[n]) + (v[n]))


print ("Soma do vetor:\n",vetor)


u = np.array(u)
v = np.array(v)

print ("Soma de vetor com Biblioteca\n",u + v)

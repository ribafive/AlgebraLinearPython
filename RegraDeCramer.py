import numpy as np
from numpy.linalg import det, inv

A = np.array ([[-1,2],[2,1]])
B = np.array ([[-1],[5]])

print(A)
print(B,"\n\n")

D = det (A)
print(D,"\n")

Ax = A.copy()
Ax[:,0] = B[:,0]
print(Ax,"\n")

Ay = A.copy()
Ay[:,1] = B[:,0]
print(Ay,"\n\n")

#calcular o determinante
Dx = det(Ax)
Dy = det(Ay)

x = Dx/D
print(x,"\n")

y = Dy/D
print(y,"\n\n")

#Sistema com três variáveis
G = np.array([[1,2,3],[6,0,1],[4,5,-1]])
H = np.array([[3],[-6],[1]])

print(G)
print(H)

Dn = det(G)
print(Dn)

Bx = G.copy() 
By = G.copy()
Bz = G.copy()

Bx[:,0] = H[:,0]
By[:,1] = H[:,0]
Bz[:,2] = H[:,0]

Dnx = det(Bx)
Dny = det(By)
Dnz = det(Bz)

X = Dnx/Dn
Y = Dny/Dn
Z = Dnz/Dn

print(X.shape,"\n",Y,"\n",Z,"\n")


import numpy as np
from  numpy.linalg import det, inv
import matplotlib.pyplot as plt


#Sistema:
#
#   y - 2x = 5
#   y + 3x = 2

A = np.array([[1,-2],[1,3]])
B = np.array([[5],[2]])

#Para representação gráfica - Distinção de Y

x = np.linspace(-10,10,100)

y1 = 2*x + 5
y2 = -3*x + 2

plt.plot(x,y1,'red')
plt.plot(x,y2,'blue')

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()

P = inv(A).dot(B)
print(P)

plt.plot(x,y1,'red')
plt.plot(x,y2,'blue')

plt.plot(P[1],P[0],'og') #og ponto verde

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()

#Sistema 2:
#
#   y3 = 2x + 4 -> y3 - 2x = 4
#   y4 = 2x + 8 -> y4 - 2x = 8

F = np.array([[1,-2],[1,-2]])
G = np.array([[4],[8]])

y3 = 2*x + 4
y4 = 2*x + 8

plt.plot(x,y3,'red')
plt.plot(x,y4,'blue')

plt.legend(["y3 = 2*x+4\tLinha vermelha" , "y4=2*x +8\tLinha Azul"])

plt.xlabel('X')
plt.ylabel('Y')

plt.show() #Não tem solução pq não tem o ponto de intersecção

print(det(F))






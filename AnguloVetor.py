import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
    """
    Plot set of vectors.

    Parameters
    ----------
    vecs : array-like
        Coordinates of the vectors to plot. Each vectors is in an array. For
        instance: [[1, 3], [2, 2]] can be used to plot 2 vectors.
    cols : array-like
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
    alpha : float
        Opacity of vectors

    Returns:

    fig : instance of matplotlib.figure.Figure
        The figure of the vectors
    """
    plt.figure()
    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                  alpha=alpha)

def ang_2vet(v,u):
    v_interno_u = v.dot(u) # .dot produto interno

    vn = np.linalg.norm(v)
    un = np.linalg.norm(u)

    r = v_interno_u / (vn * un)

    ang = np.arccos(r) #ele retorna em radianos

    return (180 / np.pi) * ang #retornar em graus

u = np.array([0,1])
v = np.array([1,0])

red = 'red'
blue = 'blue'

plotVectors ([u,v] , [red, blue])
plt.xlim(-1,5)
plt.ylim(-1,5)

plt.show()

print (ang_2vet(v,u))

u2 = np.array([1,1])
v2 = np.array([1,0])


red = 'red'
blue = 'blue'

plotVectors ([u2,v2] , [red, blue])
plt.xlim(-1,2)
plt.ylim(-1,2)

plt.show()

print (ang_2vet(u2,v2),"º")










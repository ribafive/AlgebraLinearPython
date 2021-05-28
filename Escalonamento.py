import numpy as np

M = np.array([[1.,4,3,1],[2.,5.,4.,4.],[1,-3,-2,5]])
print(M)

M[1,:] = -2*M[0,:] + M[1,:]
print(M)

M[2,:] = M[2,:] - M[0,:]
print(M)

M[1,:] = -1/3 * M[1,:]
print(M)

M[0,:] = (-4 * M[1,:]) + M[0,:]
print(M)

M[2,:] =(7 * M[1,:]) + M[2,:]
print(M)

M[2,:] = -3 *M[2,:]
print(M)

M[1,:] =  (- 0.66666666667 * M[2,:]) + M[1,:]
print(M)

M[0,:] = (-0.3333333333333 * M[2,:]) + M[0,:]
print(M)

#chegando ao resultado 3,-2, 2

#função que arredonda np.round

print(np.round(M))

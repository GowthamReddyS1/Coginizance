import numpy as np
Z = np.array([10,12,13,14,15])
nz = 5
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)
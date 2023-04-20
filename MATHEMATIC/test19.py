
 

import numpy as np
from numpy import linalg as la


v = np.array([846835985, 9834798552])
u = np.array([87502093, 123094980])

def gauss_algorithm(v1, v2):
    while True:

        size1 = la.norm(v1)
        size2 = la.norm(v2)
        if size2 < size1:
            x = v1
            v1 = v2
            v2 = x
        m = round(np.dot(v1, v2) / np.dot(v1, v1))
        if m == 0:
            return v1, v2
        v2 = np.subtract(v2, np.multiply(m, v1))
a, b = gauss_algorithm(u, v)
print(np.dot(a, b))
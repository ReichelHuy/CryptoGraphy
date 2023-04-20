import numpy as np

a = np.array([[6, 2, -3], [5, 1, 4], [2, 7, 1]])
flag = -np.linalg.det(a)
print(flag)
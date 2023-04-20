import numpy as np
v = [2,6,3]
w = [1,0,0]
u = [7,7,2]
vector1 = np.array(v)
vector2 = np.array(w)
vector3 = np.array(u)
x=(2*vector3)
y=3*(2*vector1 - vector2)
print(np.dot(y,x))
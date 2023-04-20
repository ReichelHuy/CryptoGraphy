import numpy as np 

def projete_orthogonale(u, v):
    return np.multiply((np.dot(u, v))/np.sqrt(sum(u**2)**2), u)

v1 = np.array([4,1,3,-1])
v2 = np.array([2,1,-3,4]) 
v3 = np.array([1,0,-2,7]) 
v4 = np.array([6, 2, 9, -5])

vectors_list = [v1, v2, v3, v4]

u_list = [vectors_list[0]]
for i in range(1,len(vectors_list)):
    v_i = vectors_list[i]
    u_i = v_i
    for j in range(0, i):
        u_j = u_list[j]
        u_i = u_i - projete_orthogonale(u_j, v_i)
    u_list.append(u_i)

e_list = [np.multiply(1/np.sqrt(sum(u_list[i]**2)**2), u_list[i]) for i in range(0, len(u_list))]
print(round(u_list[3][1], 5))
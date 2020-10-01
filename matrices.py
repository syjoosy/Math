import matrices_gsh as mat
import numpy as np

def GramSchmidt(*a):
    k = len(a[0])
    N = len(a)
    b = [[0] * k for i in range(N)]
    r = [[0] * k for i in range(N)]

    b[0] = a[0]
    for i in range(1,N):
        sum = a[i]
        for j in range(0,i):
            scolar_ab = 0
            scolar_bb = 0
            proj = [i for i in range(k)]
            for n in range(k):
                scolar_ab += b[j][n]*a[i][n]
                scolar_bb += b[j][n]*b[j][n]
            for n in range(k):
                proj[n] = round(((scolar_ab/scolar_bb)*b[j][n]),2)
            for n in range(k):
                sum[n] -= proj[n]
            r[i][j] = (scolar_ab/scolar_bb)

        b[i] = sum
        for j in range(k):
            r[j][j] = 1
    return b, r


m = mat.A1
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

i = 0
while i <= 9:
    exec("x{} = {}".format(i, rez[i]))
    i += 1


#Решение на Python
q, r = GramSchmidt(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9)
qn = np.transpose(q)
rn = np.transpose(r)
print(q)
print("----------------------------")
print(r)
print("----------------------------")
print(qn.dot(rn))

#Решение Numpy
q,r = np.linalg.qr(mat.A1)
print("----------------------------")
print("Numpy matrix Q")
print(q)
print("----------------------------")
print("Numpy matrix R")
print(r)
print("----------------------------")
print("Numpy matrix multiplication QR")
print(q.dot(r))


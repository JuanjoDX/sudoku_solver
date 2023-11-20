import numpy as np
from datetime import datetime
import funciones as fn

n_filas = 3
n_columnas = 3
dim = n_filas*n_columnas 
mat_cuadrante = np.arange(1, (dim+1)).reshape((n_filas, n_filas))

mat1 = np.zeros((9, 9))
mat1[0] = np.array([6,5,np.nan,np.nan,np.nan,7,9,np.nan,3])
mat1[1] = np.array([np.nan,np.nan,2,1,np.nan,np.nan,6,np.nan,np.nan])
mat1[2] = np.array([9,np.nan,np.nan,np.nan,6,3,np.nan,np.nan,4])
mat1[3] = np.array([1,2,9,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
mat1[4] = np.array([3,np.nan,4,9,np.nan,8,1,np.nan,np.nan])
mat1[5] = np.array([np.nan,np.nan,np.nan,3,np.nan,np.nan,4,7,9])
mat1[6] = np.array([np.nan,np.nan,6,np.nan,8,np.nan,3,np.nan,5])
mat1[7] = np.array([7,4,np.nan,5,np.nan,np.nan,np.nan,np.nan,1])
mat1[8] = np.array([5,8,1,4,np.nan,np.nan,np.nan,2,6])

inicio = datetime.now()
mataux = mat1.copy()
while np.sum(np.isnan(mat1)) > 0:
    for i in range(0,9):
        for j in range(0,9):
            aux = mat1[i,j]
            if np.isnan(aux):
                fn.revisar(i,j,mat1,mat_cuadrante,dim,n_filas,n_columnas)
fin = datetime.now()

print(fin-inicio)
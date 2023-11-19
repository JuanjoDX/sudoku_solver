import numpy as np
from datetime import datetime

def fun_cuadrante(mat,dim,c_aux,n_filas,n_columnas):
    c = 0
    for i in range(0,dim,n_filas):
        i_fin = i+n_filas
        for j in range(0,dim,n_columnas):
            j_fin = j+ n_columnas
            c = c + 1
            if c == c_aux:
                return(cuadrante_to_list(mat[i:i_fin,j:j_fin]))

def cuadrante_to_list(mat):
    mat_aux = mat.tolist()
    mat_aux = [elemento for sublista in mat_aux for elemento in sublista]
    return(mat_aux)


def fun_fila(pos_fila,n_filas):
    n = 1
    while True:
        if pos_fila <= n_filas*n:
            return(n)
        else:
            n = n+1
            
def fun_columna(pos_col,n_columnas):
    n = 1
    while True:
        if pos_col <= n_columnas*n:
            return(n)
        else:
            n = n+1

mat_cuadrante = np.arange(1, 10).reshape((3, 3))
n_filas = 3
n_columnas = 3


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
                print("i",i)
                print("j",j)
                fila = mat1[i]
                columna = mat1.transpose()[j]
                aux1 = fun_fila((i+1),n_filas)-1
                aux2 = fun_columna((j+1),n_columnas)-1
                cuadrante = mat_cuadrante[aux1,aux2]
                valor = set(range(1,10))-set(fila)-set(columna)-set(fun_cuadrante(mat1,9,cuadrante,n_filas,n_columnas))
                if len(valor) == 1:
                    mat1[i,j] = list(valor)[0]
                    print(mat1)
                    print("")
fin = datetime.now()

print(fin-inicio)
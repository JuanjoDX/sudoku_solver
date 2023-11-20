import pandas as pd
import numpy as np
import funciones as fn
from datetime import datetime

df = pd.read_excel('../Sudoku/ejem4_3x3.xlsx',header=None)
mat1 = df.values

n_filas = 3
n_columnas = 3
dim = n_filas*n_columnas 
mat_cuadrante = np.arange(1, (dim+1)).reshape((n_filas, n_columnas))
mat_posib = np.full((dim, dim), set(), dtype=object)

c = 0
inicio = datetime.now()
while np.sum(np.isnan(mat1)) > 0:
    for i in range(0,9):
        for j in range(0,9):
            aux = mat1[i,j]
            if np.isnan(aux):
                fn.revisar(i,j,mat1,mat_posib,mat_cuadrante,dim,c,n_filas,n_columnas)                    
    if c == 0:
        c = c+1
    fin = datetime.now()
print(fin-inicio)
import time
def retornar_cuadrante(mat,dim,c_aux,n_filas,n_columnas):
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

def posicion(pos,n):
    c = 1
    while True:
        if pos <= n*c:
            return(c-1)
        else:
            c = c+1

def componentes_cuadrante(cuadrante,n):
    ### no es realmente el cuadrante sino lo que retornan por filas y por columnas aux1 y aux2
    return(list(range(cuadrante*n - n,cuadrante*n)))

def revisar(i,j,mat1,mat_posib,mat_cuadrante,dim,c_mat_posib,n_filas,n_columnas):
    fila = mat1[i]
    columna = mat1.transpose()[j]
    aux1 = posicion((i+1),n_filas)
    aux2 = posicion((j+1),n_columnas)
    cuadrante = mat_cuadrante[aux1,aux2]
    valor = set(range(1,(dim+1)))-set(retornar_cuadrante(mat1,dim,cuadrante,n_filas,n_columnas))-set(fila)-set(columna)
    if len(valor) == 1:
        print("prueba1: fila",i,"columna",j)
        print(valor)
        mat1[i,j] = list(valor)[0]
        print(mat1)
        print("")
    else:
        filas_contiguas = componentes_cuadrante((aux1+1),n_filas)
        columnas_contiguas = componentes_cuadrante((aux2+1),n_columnas)
        filas_contiguas.remove(i)
        columnas_contiguas.remove(j)
        aux1_fila = (mat1[filas_contiguas[0]])
        aux2_fila = (mat1[filas_contiguas[1]])
        aux1_columas = (mat1.transpose()[columnas_contiguas[0]])
        aux2_columas = (mat1.transpose()[columnas_contiguas[1]])
        mat_filas = set(aux1_fila) & set(aux2_fila)
        mat_columnas = set(aux1_columas) & set(aux2_columas)
        # print(set(mat_filas))
        # print(set(mat_columnas))
        # print(valor)
        # print((set(mat_filas) & (valor)) & (set(mat_columnas) & valor))
        valor2 = ((set(mat_filas) & (valor)) & (set(mat_columnas) & valor))
        if len(valor2) == 1:
            print("prueba2: fila",i,"columna",j)
            print(valor2)
            mat1[i,j] = list(valor2)[0]
            print(mat1)
            print("")
        else:
            mat_posib[i,j] = valor
            if c_mat_posib == 1:
                aux_mat_pos = mat_posib[i,j]
                auxiliar = retornar_cuadrante(mat_posib,dim,cuadrante,n_filas,n_columnas)
                unicos = []
                for k in auxiliar:
                    if k not in unicos:
                        unicos.append(k)

                aux2 = auxiliar.copy()
                aux2.remove(aux_mat_pos)
                aux_unicos = aux_mat_pos - set.union(*aux2)
                if len(aux_unicos) == 1:
                    print("prueba3: fila",i,"columna",j)
                    print(aux_unicos)
                    mat1[i,j] = list(aux_unicos)[0]
                    print(mat1)
                    print("")

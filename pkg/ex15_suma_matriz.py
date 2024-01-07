"""Función que suma matrices"""
def suma_matriz(matriz1:list,matriz2:list):
    """
    Suma de vectores

    Args:
        matriz1 (list): Matriz 1 a Sumar
        matriz2 (list): Matriz 2 a Sumar

    Raises:
        ValueError: Las matrices deben tener la misma cantidad de filas y columnas.
    
    Return: Imprime el resultado de la suma.
    """
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if filas_matriz1 != filas_matriz2 or columnas_matriz1 != columnas_matriz2:
        raise ValueError("Las matrices deben ser de tener la misma longitud")

    resultado = [[0 for _ in range(columnas_matriz1)] for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz1):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return print("El resultado de sumar las matrices es : ",resultado)

matriz_A = [[1,4,7],
            [2,5,8],
            [3,6,9]]

matriz_B = [[9,6,3],
            [8,5,2],
            [7,4,1]]

if __name__ =='__main__':
    suma_matriz(matriz_A,matriz_B)

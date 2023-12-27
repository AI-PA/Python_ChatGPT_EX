"""Algoritmos de ordenamiento de listas"""
import random

def Merge(left_array, right_array):
    """
    Ordenamiento de las divisiones del algoritmo, compara los dos arrays y toma el menor. Lo 
    agrega a la lista y lo elimina asi hasta terminar con los elementos del array. 
    
    En el caso base, se agrega a la array y se retorna la función. 

    Args:
        left_array  (list : int, float ): la division del array de Inicio a la Mitad. 
        right_array (list : int, float ): la division del mayor de la Mitad hasta el Final.

    Returns:
        arr_result: regresa el array ordenado.
    """
    arr_result =[]
    while len(left_array)>0 and len(right_array)>0:
        if left_array[0] > right_array[0]:
            arr_result.append(right_array[0])
            right_array.pop(0)
        else:
            arr_result.append(left_array[0])
            left_array.pop(0)
    while len(left_array)>0:
        arr_result.append(left_array[0])
        left_array.pop(0)

    while len(right_array)>0:
        arr_result.append(right_array[0])
        right_array.pop(0)
    return arr_result

def mergeSort(arr):
    """
    Uso del Algoritmo merge sort para ordenar listas, se trata de dividir hasta un caso base, 
    para después ir armando un array de manera ordenada. 
    1.Divide. 
    2.Vencerás. 
    3.Union.
    Args:
        arr (int,float,str): Ordena la lista proporcionada

    Returns:
        Regresa la Union de los elementos una vez ordenada.
    """
    if len(arr)==1:
        return arr

    middle = len(arr)//2
    left_array = arr[:middle]
    right_array =arr[middle:]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    return Merge(sorted_left_array,sorted_right_array)

def get_random_array():
    """
    Uso de la librería random para generar números aleatorios e introducirlos a un array. 
    para después ordenarlos. 

    Returns:
        arr: imprime el array ordenado por el algoritmo de Merge Sort.  
    """
    array_aleatorio = [random.randint(1, 1000) for _ in range(100)]
    print(f"el array es : {array_aleatorio} \n")
    return print(f"\n el array ordenado es queda asi : {mergeSort(array_aleatorio)}")

def get_array():
    """
    Genera un array en base a los elementos que el usuario selecciona
    para después ordenarlos.

    Returns:
        Regresa el array ordenado por el algoritmo Merge Sort
    """
    number_of_elements = int(input("Cuantos elementos quieres en el array: "))
    array=[]
    for i in range (0,number_of_elements):
        array.append(int(input("Teclea un numero : ")))
    print(f"El array es : {array} \n" )
    return print(f"\n el array ordenado es queda asi : {mergeSort(array)}")

def choose():
    """
    Permite elegir si se genera un array aleatorio. 
    o se introduce uno por el usuario.
    
    """
    user_option= int(input(""" Selecciona una opción:
                        1 -. Generar un array y ordenarlo.
                        2 -. Tomar un array aleatorio y ordenarlo.
                        """))
    if user_option == 1:
        get_array()
    else:
        get_random_array()

if __name__=='__main__':
    choose()

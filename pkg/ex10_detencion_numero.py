"""Generar una función que cuente cuales números están en la lista y la frecuencia de los mismos."""
import random
def contador_num(lista:list):
    """
    Toma la lista, elimina los valores repetidos y se guarda como una nueva lista, posteriormente
    se ejecuta un ciclo para saber la frecuencia de los números. 
    Args:
        lista (list): lista de números a contar. 

    Returns:
        dict: diccionario con los números y la frecuencia en la que están en la lista. 
    """
    new_list =set(lista)
    count_elements =[]
    for element in new_list:
        count_elements.append(lista.count(element))
    return dict(zip(new_list,count_elements))

def generar_numeros():
    """
    generación de una lista aleatoria de números. 
    y un diccionario con los números y su frecuencia. 
    """
    numeros = [random.randint(1,50) for i in range(100)]
    print (f"la lista de numeros es : {numeros} \n\n")
    print(f" y la frecuencia en la que aparecen los números es la siguiente: {contador_num(numeros)}")

if __name__ =='__main__':
    generar_numeros()

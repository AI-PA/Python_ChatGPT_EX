"""Función que se encarga de contar las palabras de un texto"""
def contador_palabras(string :str):
    """
    Contador de palabras que tiene un string

    Args:
        string (str): texto que introduce el usuario

    Returns:
        integer: Numero de elementos del array, utilizando split para el texto 
    """
    return len(string.split())

def texto_y_numero():
    """
    Permite la entrada de texto, para después contar la cantidad de palabras que tiene
    llamando a otra función que se encarga de ello. 
    Returns:
        salida a consola: de la entrada de texto y el numero de palabras.
    """
    text = input(" Inserte un texto : ")
    return print(f"\n El numero de palabras es {contador_palabras(text)}, del Texto: \n \t {text} \n")

if __name__ == '__main__':
    texto_y_numero()

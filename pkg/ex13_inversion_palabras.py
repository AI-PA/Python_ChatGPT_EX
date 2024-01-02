"""Función para voltear el texto"""
def inversion_palabras():
    """
    Función que se encarga de voltear palabra por palabra un texto
    introducido por el usuario. 

    Returns:
        print: texto volteado. 
    """
    text=input("Introduce una palabra o texto: ")
    text=text.split()
    for i, word in enumerate(text):
    # El método enumerate permite hacer una tuple para cada elemento estilo (1, word)
    # permitiendo hacer un for mas rápido y modificar sus valores sin confundirnos.
        text[i] = word[::-1]

    text = " ".join(text)
    return print(f"El texto o palabra volteado es :  \n \t {text}")

if __name__ =='__main__':
    inversion_palabras()

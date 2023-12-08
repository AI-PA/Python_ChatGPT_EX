"""
Funcion parte del packaing. 
Crea una función que cuente el número de vocales en una cadena de texto.
"""
def count_vocales():
    """
    La funcion cuenta la cantidad de vocables que hay por cada vocal y 
    tambien la cantidad total de un texto o palabra.
    """
    vocals = ['a','e','i','o','u']
    text=input("Inserte un texto o palabra: ")

    # Creacion de diccionario para contar las vocables.
    vocal_counts = {v:0 for v in vocals}
    for char in text:
        if char.lower() in vocals:
            vocal_counts[char.lower()]+=1
    print(f"Del texto anterior la cantidad de vocales que hay son:  {sum(vocal_counts.values())}")
    print("La cantidad de: ")
    print(vocal_counts)

#Para poder ejecutar la funcion por separado y por pck.
if __name__=='__main__':
    count_vocales()

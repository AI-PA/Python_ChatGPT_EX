"""
Funcion para ser parte del packaing. Escribe un programa que verifique 
si una palabra es un palíndromo (se lee igual de izquierda a derecha 
que de derecha a izquierda)
"""
def palindromo():
    """funcion que identifica si una palabra es palindromo. 
    """
    string = input("Teclea una palabra: ")
    if string == string[::-1]:
        print(f"La palanra {string} es un palindromo :) ")
    else:
        print(f"La palanra {string} no es un palindromo :( ")

if __name__ =="__main__":
    palindromo()

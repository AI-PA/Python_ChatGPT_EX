"""
Funcion para ser parte del packaing. 
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

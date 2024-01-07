"""Generador de contraseñas"""
import random

def lista_caracter(mayuscula:bool,numero:bool,alfanumericos:bool):
    words="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    numbers="0 1 2 3 4 5 6 7 8 9"
    alphanumeric=""""~ ! @ # $ % ^ & * ( ) _ + [ ] \ ; ' : / , . < > ? : { | } ="""

    if mayuscula: 
        words+=words.upper()
    if numero:
        words+=numbers
    if alfanumericos:
        words+= alphanumeric
    return words.split()


def generador_contrasena():
    """
    Pregunta al usuario que tipo de contraseña necesita.

    Returns:
        print, str: Regresa la contraseña generada
    """
    num_caracteres = int(input("Tecle el numero de caracteres para generar la contraseña: "))
    mayuscula = bool(int(input("Seleccione 1 si quiere Mayúsculas o 0 si no quiere mayúsculas: ")))
    numeros =bool(int(input("Seleccione 1 si quieres Números o 0 si no quiere números: ")))
    alfanumericos =bool(int(input("Seleccione 1 si quiere caracteres especiales o 0 si no quieres: ")))
    password = []

    for _ in range(num_caracteres):
        password.append(random.choice(lista_caracter(mayuscula,numeros,alfanumericos)))
    return print(" Tu contraseña es: ","".join(password))

if __name__ =="__main__":
    generador_contrasena()

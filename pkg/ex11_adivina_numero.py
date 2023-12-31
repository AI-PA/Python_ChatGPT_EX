"""Función que contiene el juego de adivina el numero. """
import random
def adivina_numero():
    """
    Juego de adivina el numero
    Returns:
        print: Las felicitaciones del usuario por  adivinar el numero. 
    """
    num_random = random.randint(1,50)
    num_usuario = ""
    print("Escoge un numero del 1 al 50")
    while num_random != num_usuario:
        num_usuario=int(input("Tecle un numero: "))
        if num_usuario > num_random:
            print("Es un poquito mas abajo ⬇️ \n")
        else:
            print("Es mas arriba ⬆️\n")
    return print(f"Felicidades adivinaste el numero :) era {num_usuario}")

if __name__ == '__main__':
    adivina_numero()

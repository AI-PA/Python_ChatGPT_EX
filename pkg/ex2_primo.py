"""
Generacion de funcion que permite identificar si el numero dado pertenece a los numeros primos.
siendo parte del packaing principal.  
"""

def primo():
    """La funcion se encarga de comprobar si el numero que inserta el usuario es primo o no"""
    num = int(input("Tecle el numero a identificar si es primo: "))
    for i in range(2,num):
        if((num%i == 0) and (i != num or i != 1)):
            return print(f"El numero {num} no es primo :( ")
    return print(f"El numero {num} es primo :) ")

if __name__ =='__main__':
    primo()

"""Calculadora de potencias sin usar el operador de potencia"""
def calculadora_potencias(num:int,potencia:float):
    """
    Se asigna el numero de la potencia a una variable que llamaremos constante, 
    mientas que se multiplica la variable num las veces que marca la potencia. 

    Args:
        num (int): Numero que el usuario quiere saber su potencia.
        potencia (float): Base que se va a multiplicar el numero.

    Returns:
        num (int): Potencia que usuario quiere saber. 
    """
    const = num
    for i in range (1,potencia):
        num=num*const
    return num

def potenciar_numero():
    """
    Pregunta por el numero del usuario y 
    llama a la función para calcular su potencia. 
    
    Returns:
        print: La potencia del numero introducían en la base requerida.
    """
    num = int(input("Teclea un numero que quieres saber su potencia: "))
    potencia =int(input("Escoge una base, tiene que ser mayor a 0: "))
    return print(f" la potencia del numero {num} es  {calculadora_potencias(num,potencia)}")

if __name__=="__main__":
    potenciar_numero()

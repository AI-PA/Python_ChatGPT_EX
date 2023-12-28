"""Diseño de un algoritmo recursivo para calcular el factorial de un numero"""

def factorial(n):
    """
    Algoritmo recursivo para el factorial, llegando al caso base 0 o 1, que su factorial
    es 1 y a partir de hay regresa los valores hasta calcular el factorial deseado. 

    Args:
        n (int): Numero que queremos saber su factorial. 

    Returns:
        factorial(n-1) * n: la multiplicación del numero que queremos por el factorial anterior
                            para calcular el factorial deseado.
    """
    if n == 0 or n==1:
        return 1
    else:
        return factorial(n-1)*n

def factorial_print():
    """Impresión de valores de la función factorial."""
    number = int(input("Tecle el numero a calcular el factorial: "))
    print(f"\n El factorial de {number} es : {factorial(number)}")

if __name__=='__main__':
    factorial_print()

"""Implementa una función que genere los primeros N términos de la secuencia de Fibonacci"""

def Fibonacci(n):
    """Función Fibonacci recursiva

    Args:
        n (int): numero anterior de la serie hasta llegar al caso base. 

    Returns:
        _type_: en caso base el numero de la serie que seria 0 o 1,
                en el resto la función en n-1 y n-2 hasta llegar al caso base.
    """
    if n < 2:
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)

def Posicion_Fibonachi():
    """
    Comando que retiene los valores de la serie y de Fibonacci.
    """
    n= int(input("Tecle la posicion de Fibonacci: "))
    serie= []
    for i in range(0,n+1):
        serie.append(Fibonacci(i))
    print(f"""La serie de Fibonacci es : {serie}
            el valor pedido es : {Fibonacci(n)}
            """)

if __name__=='__main__':
    Posicion_Fibonachi()

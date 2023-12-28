"""_summary_"""

def Fahrenheit_Or_Celsius(n:float ,choose:int):
    """_summary_

    Args:
        n (int): _description_
        choose (int): _description_

    Returns:
        _type_: _description_
    """
    if choose == 1:
        return (n-32)*(5/9)
    return (n*(9/5)) +32

def Conversor_Temperatura():
    """Toma de valores para ejecutar, el cambio de temperatura.
    """
    choose = int(input("Selecciona a que temperatura quieres convertir: \n 1.-Fahrenheit a Celsius \n 2.- Celsius a Fahrenheit \n"))
    temperatura = int(input("Teclea la temperatura a convertir: "))
    if choose ==1:
        print(f"La Temperatura de {temperatura} °F es: {Fahrenheit_Or_Celsius(temperatura,choose)} °C")
    else:
        print(f"La Temperatura de {temperatura} °C es: {Fahrenheit_Or_Celsius(temperatura,choose)} °F")

if __name__=='__main__':
    Conversor_Temperatura()

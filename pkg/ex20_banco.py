"""Simulación de operaciones de un cajero"""
import random

def deposito(saldo:int,tarjeta:int):
    """Deposito a la cuenta de de la tarjeta

    Args:
        saldo (int): cantidad disponible en la cuenta
        tarjeta (int): últimos 3 números de la tarjeta
    """
    print("preparando maquina para recibir el deposito \n\n\n\n\n")
    money=int(input("Cuanto dinero va a depositar: "))
    saldo+= money

    print("Deposite el dinero...")
    print("Calculando saldo.......")
    print(f"Actualmente tiene un saldo de ${saldo} \n\n")
    operaciones(saldo,tarjeta)

def retiro(saldo:int,tarjeta:int):
    """Retiro de una cuenta de banco

    Args:
        saldo (int): dinero disponible
        tarjeta (int): últimos 3 números de la cuenta
    """
    print(f"El saldo disponible es {saldo}")
    if saldo < 50:
        print("No contamos con billetes mas chicos de $50")
    retiro_saldo = int(input("Tecle la cantidad a retirar: "))
    if saldo//50 != 0:
        print("Escoge otra cantidad que se pueda repartir en billetes de $50, $100, $200")

    retiro_saldo = int(input("Tecle la cantidad a retirar: "))
    saldo-=retiro_saldo
    print(f"Su saldo disponible es: ${saldo}")
    operaciones(saldo,tarjeta)


def consulta(saldo:int,tarjeta:int):
    """Genera una consulta de saldo

    Args:
        saldo (int): cantidad de dinero disponible
        tarjeta (int): últimos 3 dígitos de la cuenta
    """
    print(f"El saldo disponible es: ${saldo}")
    operaciones(saldo,tarjeta)

def transferencia(saldo:int ,tarjeta:int):
    """Genera una trasferencia a una cuenta

    Args:
        saldo (int): Dinero disponible
        tarjeta (int): últimos 3 dígitos de la cuenta
    """
    print(f"Saldo disponible {saldo}")
    cuenta_transferencia =" Tecle la cuenta a transferir: "
    cantidad_transferir ="Tecle la cantidad  a transferir: "
    if cantidad_transferir < saldo:
        saldo -= cantidad_transferir
        print(" Transferencia Exitosa  ")
        print(f" la transferencia de la cuenta *{tarjeta} a la cuenta *{cuenta_transferencia[-3:]}")
        print(f" por la cantidad de ${cantidad_transferir}")

        operaciones(saldo,tarjeta)
    else:
        print("Operación Fallida, Saldo no disponible :l ")


def banco():
    """Función principal del modulo"""
    tarjeta =random.randint(100,999)
    print(".............................")
    print("Lectura exitosa :)  \n\n\n\n\n\n\n\n\n")
    print(f"Tarjeta con terminación *{tarjeta}")
    print("Hola, Bienvenido a Banco Patito SA de CV. \n En que podemos ayudarle")
    saldo = random.randint(1,1999999)
    operaciones(saldo,tarjeta)

def operaciones(saldo:int,tarjeta:int):
    """Encargada de almacenar y llamar las operaciones de un banco"""
    option =0
    while option !=5:
        print("\n\n")
        print(""" Opciones Disponibles en su cuenta:
                    1.- Deposito
                    2.- Retiro
                    3.- Consultar Saldo
                    4.- Transferencia
                    5.- Salir \n\n""")
        option =int(input("Seleccione una opción : "))
        #LLamada de funciones a procesar.
        if 1<= option <=5:
            if option ==1:
                deposito(saldo,tarjeta)
            if option ==2:
                retiro(saldo,tarjeta)
            if option ==3:
                consulta(saldo,tarjeta)
            if option ==4:
                transferencia(saldo,tarjeta)
        else:
            print("Opción no valida. Inténtalo de nuevo:")
    print("Hasta Luego :)")

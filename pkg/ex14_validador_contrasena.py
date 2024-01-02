"""Función para validad contraseñas"""
def longitud(text:str):
    if len(text) >= 8 and len(text) <= 15:
        return True
    return False

def numeros(text:str):
    num="1234567890"
    for letter in text:
        if letter in num:
            return True
    return False

def caracteres_especial(text:str):
    caracteres="!@#$%^&*()/"
    for letter in text:
        if letter in caracteres:
            return True
    return False

def letra_minuscula(text:str):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter in abecedario:
            return True
    return False

def letra_mayuscula(text:str):
    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in text:
        if letter in abecedario:
            return True
    return False


def validador_contrasena():
    print(""" Bienvenido al validador de contraseñas
            Validaremos que tu contraseña cumpla con las siguientes características. 
            -Longitud de 8 a 15 Caracteres
            -Presencia de números
            -Al menos una letra minúscula
            -Al menos una letra mayúscula
            -Al menos uno de los siguientes caracteres : !@#$%^&*()/ \n""")
    text=input("Inserta tu contraseña: ")
    validaciones=[]
    validaciones.append(longitud(text))
    validaciones.append(numeros(text))
    validaciones.append(letra_minuscula(text))
    validaciones.append(letra_mayuscula(text))
    validaciones.append(caracteres_especial(text))

    errores = {
                0:"Longitud no valida",
                1:'No Contiene números',
                2:'No Contiene letras minúsculas',
                3:'No Contiene letras mayúscula',
                4:'No Contiene caracteres especiales'
    }
    for i,value in enumerate(validaciones):
        if not value:
            print(errores.get(i))
            break
    print(f"La contraseña: {text} pasa todos los test :) ")

if __name__ =="__main__":
    validador_contrasena()

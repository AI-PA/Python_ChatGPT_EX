#Calculadora Simple
#Crea un programa que realice operaciones básicas como suma, resta, multiplicación y división.
def calculadora():
     # Definicion de Operaciones a realizar. 
     operation = {
                    1:lambda a,b: a+b,
                    2:lambda a,b: a-b,
                    3:lambda a,b: a*b,
                    4:lambda a,b: a/b,
                    5:lambda a,b: a**b,
                    6:lambda a: a**0.5
               }
     # Entradas del Usuario. 
     print("""
          Bienvenido a la calculadora de Python. 
               podemos realizar las siguientes operaciones: 
                    1.- Suma.
                    2.- Resta. 
                    3.- Multiplicación. 
                    4.- Division. 
                    5.- Potencia
                    6.- Raíz cuadrada.
          """)
     option =int(input("Inserte el numero de la operación a realizar: "))
     
     if (option in [1,2,3]):
          num1 =int(input("Teclea el numero 1: ")) 
          num2 =int(input("Teclea el numero 2: "))
     elif(option == 4):
          num1 =int(input("Teclea el numerodor: ")) 
          num2 =int(input("Teclea el denominador: "))
     elif(option == 5):
          num1 =int(input("Teclea el numero base: ")) 
          num2 =int(input("Teclea el numero potencia: "))
     elif(option == 6):
          num1 =int(input("Teclea el numero: ")) 
          num2=None

#Buscar la funcion en el diccionario y pasar los balores.           
     if option in operation:
          print(f"El Resultado es: {operation[option](num1,num2)}")
     else: 
          print("Teclea una opcion valida: ")

if __name__ =='__main__':
     calculadora()
"""Búsqueda de archivos repetidos """
import os
def archivos():
    """Búsqueda de archivos repetidos, tomando la función OS

    Returns:
        list: documentos repetidos
    """
    archivos1 = os.listdir(input("Dame una ruta de archivos: "))
    archivos2 = os.listdir(input("Dame una ruta de archivos: "))
    archivos_duplicados =[]
    for i in archivos1:
        for a in archivos2:
            if i==a:
                print("Se repiten los archivos",a,i)
                archivos_duplicados.append(a)
    return print("los archivos duplicados fueron : ", archivos_duplicados)
if __name__ =="__main__":
    archivos()

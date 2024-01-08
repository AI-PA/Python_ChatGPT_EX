def cifrado_cesar():
    alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    mensaje = input("Escriba el mensaje a cifrar : ")
    clave = int(input("Cual sera la clave (num del 1 al 27): "))
    cifrado =""

    for letra in mensaje.upper():
        if letra in alfabeto:
            indice = alfabeto.find(letra)
            indice+=clave
            if indice>=27:
                indice -=27
            cifrado +=alfabeto[indice]
        else:
            cifrado+=letra
    return print(f"La clave es {clave} \nEl mensaje es : {cifrado}.")

if __name__ == "__main__":
    cifrado_cesar()

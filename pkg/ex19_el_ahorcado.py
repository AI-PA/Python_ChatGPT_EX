"""Juego del Ahorcado"""
import random
import string

palabras = ["aire", "ojos", "piel", "anteojos", "joven", "viejo", "alto", "bajo", "pequeño", "gordo", "delgado", "bella", "azul", "verde", "negro", "sombrero", "guantes", "corbata", "gemelos", "paraguas", "plata", "oro", "perla", "diamante", "esmeralda", "anillo", "pulsera", "reloj", "elegante", "sencillo", "chaqueta", "traje", "camisa", "zapatos", "pelo", "maquillaje", "peine", "dedo", "hueso", "cara", "ojo", "calor", "ambulancia", "enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "orgullo", "timidez", "valiente", "aburrido", "loco", "divertido", "bueno", "feliz", "amable", "pobre", "serio", "extraño", "gritar", "llorar", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "ajo", "perejil", "menta", "canela", "mayonesa", "pan", "mantequilla", "miel", "manzana", "pera", "durazno", "cereza", "papa", "lechuga", "arroz", "pollo", "pavo", "hamburguesa", "camarones", "tortilla", "espagueti", "sopa", "helado", "chocolate", "galletas", "bombones", "limpiar", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "precio", "recibo", "ascensor", "esquiar", "ciclismo", "golf", "pelota", "tenis", "bicicleta", "estadio", "gol", "torneo", "leer", "dibujar", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "fiesta", "vela", "alfombra", "puerta", "ventana", "cortina", "escritorio", "cuadro", "juguete", "alquiler", "mudanza", "casa", "pared", "chimenea", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "erizo", "mariposa", "foca", "tigre", "cobra", "almeja", "paloma", "cisne", "mosquito", "hormiga", "llover", "nevar", "nublado", "soleado", "clima", "rayo", "nieve", "sol", "viento", "padre", "madre", "hijo", "abuela", "estudioso", "aula", "tiza", "regla", "computadora", "diccionario"]
vidas_diccionario_visual = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras)  

    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra) 
    abecedario = set(string.ascii_uppercase) 
    letras_adivinadas = set()  

    vidas = 7

    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

        letra_usuario = input('Escoge una letra: ').upper()

      
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
          
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

   
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


if __name__ == '__main__':
    ahorcado()
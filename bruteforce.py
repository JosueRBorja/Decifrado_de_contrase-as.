import time
import itertools

def fuerza_bruta(contrasenia, long_max=8):
    alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~"
    intentos = 0
    inicio = time.time()

    for longitud in range(1, long_max + 1):
        print("Probando longitud", longitud, "...")
        for intento in itertools.product(alfabeto, repeat=longitud):
            intentos += 1
            intento_s = ''.join(intento)
            if intento_s == contrasenia:
                fin = time.time()
                print("Contraseña encontrada:", intento_s)
                print("Intentos:", intentos)
                print("Tiempo:", fin - inicio, "segundos")
                return intento_s
    fin = time.time()
    print("No se encontró la contraseña dentro del límite.")
    print("Intentos realizados:", intentos)
    print("Tiempo total:", fin - inicio, "segundos")
    return None

# --- uso: pedir la contraseña al usuario ---
contrasenia = input("Escribe la contraseña máx 8 caracteres: ")
encontrada = fuerza_bruta(contrasenia, long_max=8)
print("Resultado:", encontrada)

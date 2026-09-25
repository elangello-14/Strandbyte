import Proyecto_1 as p1
import Proyecto_2 as p2

# Funcionalidades
def base_mas_frecuente(cadena):
    base = max(set(cadena), key=cadena.count)
    return base

# Interacción Sistema <-> Usuario
chars_aceptados = {'A','T','G','C'}

# Inputs y resultados
if __name__ == "__main__":
    while True:
        secuencia = input("Escribe la secuencia de ADN: ")
        secuencia = secuencia.upper()
        if set(secuencia).issubset(chars_aceptados) == False:
            print("Secuencia de ADN incorrecta")
        else: break
    
    print("Secuencia de ADN válida!")
    print(f"Longitud: {p1.longitud_secuencia(secuencia)}")
    print(p1.conteo_secuencia(secuencia))
    print(f"El porcentaje GC es {round(p2.calculadora_GC(secuencia), 2)}%")
    print(f"La base más frecuente es {base_mas_frecuente(secuencia)}")

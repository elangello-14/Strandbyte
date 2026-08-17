import Proyecto_1 as p1

# Input de Secuencia
secuencia = input("Escribe la secuencia de ADN: ")

secuencia = secuencia.upper()

# Funcionalidades
def calculadora_GC(cadena):
    porcentaje = (cadena.count("G") + secuencia.count("C")) * 100 / p1.longitud_secuencia(secuencia)
    return porcentaje

print(f"El porcentaje GC es {round(calculadora_GC(secuencia), 2)}%")
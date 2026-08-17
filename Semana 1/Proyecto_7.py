import Proyecto_1 as p1
import Proyecto_2 as p2

# Funcionalidades
def base_mas_frecuente(cadena):
    regla = {
        cadena.count("A"): 'A',
        cadena.count("T"): 'T',
        cadena.count("G"): 'G',
        cadena.count("C"): 'C',
    }

    cantidad_bases = (regla[cadena.count("A")], regla[cadena.count("T")], regla[cadena.count("C")], regla[cadena.count("G")])

    return max(cantidad_bases)

# Interacción Sistema <-> Usuario
chars_aceptados = {'A','T','G','C'}

while True:
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    if chars_aceptados != set(secuencia):
        print("Secuencia de ADN incorrecta")
    else: 
        print("Secuencia de ADN válida!")
        break

print(f"Longitud: {p1.longitud_secuencia(secuencia)}")
print(p1.conteo_secuencia(secuencia))
print(f"El porcentaje GC es {round(p2.calculadora_GC(secuencia), 2)}%")
print(f"La base más frecuente es {base_mas_frecuente(secuencia)}")

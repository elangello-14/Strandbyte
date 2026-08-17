# Input de Secuencia
secuencia = input("Escribe la secuencia de ADN: ")

secuencia = secuencia.upper()

# Funciones
def longitud_secuencia(cadena):
    longitud = len(cadena)
    return longitud

def conteo_secuencia(cadena):
    A = cadena.count("A")
    T = cadena.count("T")
    C = cadena.count("C")
    G = cadena.count("G")

    return f'''
A: {A}
T: {T}
C: {C}
G: {G}'''

# Resultado
print(f"Longitud: {longitud_secuencia(secuencia)}")
print(conteo_secuencia(secuencia))




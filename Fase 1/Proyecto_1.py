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

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    
    print(f"Longitud: {longitud_secuencia(secuencia)}")
    print(conteo_secuencia(secuencia))



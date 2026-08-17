import Proyecto_3 as p3

# Input de Secuencia
secuencia = input("Escribe la secuencia de ADN: ")

secuencia = secuencia.upper()

# Funcionalidades
def cadena_complementaria_inversa(cadena):
    cadena_a_invertir = p3.cadena_complementaria(cadena)
    return cadena_a_invertir[::-1]

print(f"La cadena complementaria inversa es: {cadena_complementaria_inversa(secuencia)}")
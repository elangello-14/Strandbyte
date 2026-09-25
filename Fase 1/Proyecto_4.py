import Proyecto_3 as p3

# Funcionalidades
def cadena_complementaria_inversa(cadena):
    cadena_a_invertir = p3.cadena_complementaria(cadena)
    return cadena_a_invertir[::-1]

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(f"La cadena complementaria inversa es: {cadena_complementaria_inversa(secuencia)}")
# Funcionalidades
chars_aceptados = {'A','T','G','C'}

def validar_secuencia(cadena):
    if chars_aceptados != set(cadena):
        return False
    else:
        return True

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(validar_secuencia(secuencia))
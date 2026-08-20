# Funcionalidades
chars_aceptados = {'A','T','G','C'}

def validar_secuencia(cadena):
    cadena = set(cadena)
    if cadena.issubset(chars_aceptados):
        return True
    else:
        return False

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(validar_secuencia(secuencia))
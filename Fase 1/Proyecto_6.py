# Funcionalidades
chars_aceptados = {'A','T','G','C'}
chars_ambiguos = {'N', 'R', 'Y', 'W', 'S'}

def validar_secuencia(cadena):
    cadena = set(cadena)
    if cadena.issubset(chars_aceptados):
        if cadena.issubset(chars_ambiguos):
            return "True_chars_ambiguos"
        else:
            return True
    else:
        return False

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(validar_secuencia(secuencia))
# Funcionalidades
chars_aceptados = {'A','T','G','C'}
chars_ambiguos = ['N', 'R', 'Y', 'W', 'S']

def validar_secuencia(cadena):
    cadena = set(cadena)
    if cadena.issubset(chars_aceptados):
            return True
    else:
        for char_ambiguo in chars_ambiguos:
            if char_ambiguo in cadena:
                return "True_chars_ambiguos"
            else:
                return False

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(validar_secuencia(secuencia))
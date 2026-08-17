# Funcionalidades
chars_aceptados = {'A','T','G','C'}

# Inputs
while True:
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    if chars_aceptados != set(secuencia):
        print("Secuencia de ADN incorrecta")
    else: 
        print("Secuencia de ADN válida!")
        break
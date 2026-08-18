# Funcionalidades
def traducir_a_ARN(cadena):
    secuencia_ARN = cadena.replace("T", "U")
    return secuencia_ARN

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Introduce la secuencia de ADN para traducir a ARN: ")
    secuencia = secuencia.upper()
    print(f"Secuencia ARN: {traducir_a_ARN(secuencia)}")
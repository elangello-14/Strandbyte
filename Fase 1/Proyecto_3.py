# Reglas
complemento = {
    'A': "T",
    'G': "C",
    'T': "A",
    'C': "G"
}

def cadena_complementaria(cadena):
    cadena_complementaria = []
    for nucleotido in cadena:
        cadena_complementaria.append(complemento[nucleotido])
    return "".join(cadena_complementaria)

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(f"La cadena complementaria es: {cadena_complementaria(secuencia)}")
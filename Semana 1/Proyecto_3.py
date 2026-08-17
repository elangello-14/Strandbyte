# Input de Secuencia
secuencia = input("Escribe la secuencia de ADN: ")

secuencia = secuencia.upper()

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

print(f"La cadena complementaria es: {cadena_complementaria(secuencia)}")
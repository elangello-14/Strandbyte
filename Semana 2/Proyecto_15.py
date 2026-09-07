import Proyecto_14 as p14
import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore
from collections import Counter

# Funcionalidades
def kmer_mas_frecuente(cadena):
    kmers_a_contar = p14.mostrar_kmers(cadena).split(" ")
    contador = Counter(kmers_a_contar)
    kmer_mas_frecuente = max(contador, key=lambda k: contador[k])
    return f"El kmer más frecuente es: {kmer_mas_frecuente} --> {kmers_a_contar.count(kmer_mas_frecuente)}"

# Inputs y resultados
if __name__ == "__main__":
    while True:
        secuencia_adn = input("Escribe la secuencia de ADN: ")
        secuencia_adn = secuencia_adn.upper()
        
        if p6.validar_secuencia(secuencia_adn): print(kmer_mas_frecuente(secuencia_adn))
        else: print("Secuencia de ADN inválida")
import Proyecto_14 as p14
import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6
from collections import Counter

# Inputs y resulatados
if __name__ == "__main__":
    while True:
        secuencia_adn = input("Escribe la secuencia de ADN: ")
        secuencia_adn = secuencia_adn.upper()
        
        if p6.validar_secuencia(secuencia_adn):
            kmers_a_contar = p14.mostrar_kmers(secuencia_adn).split(" ")
            print(f"El kmer más frecuente es: {max(Counter(kmers_a_contar))} --> {max(kmers_a_contar.count(max(Counter(kmers_a_contar))))}")
        
        else: print("Secuencia de ADN inválida")
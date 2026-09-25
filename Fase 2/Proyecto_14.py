import sys
sys.path.append("Fase 1")
import Proyecto_6 as p6 # type: ignore


def mostrar_kmers(cadena):
    try:
        k = int(input("Escribe la longitud de los kmers: "))
        if k > len(cadena) or k < 1: 
            return "Longitud de los kmers inválida"
        
        else: 
            kmers = [cadena[i:(i+k)] for i in range(0, len(cadena) - k + 1)]
            return " ".join(kmers)

    except ValueError:
        return "Escribe un número válido"

# Inputs y resultados
if __name__ == "__main__":
    while True:
        secuencia_adn = input("Escribe la secuencia de ADN: ")
        secuencia_adn = secuencia_adn.upper()
        
        if p6.validar_secuencia(secuencia_adn): 
            print(mostrar_kmers(secuencia_adn))
        
        else: print("Secuencia de ADN inválida")


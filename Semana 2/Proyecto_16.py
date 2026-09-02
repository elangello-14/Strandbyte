#  🎯 Objetivo
# Crear un programa que reciba dos secuencias de ADN de igual longitud y genere un informe indicando:
    # La posición de cada nucleótido.
    # El nucleótido de cada secuencia.
    # Si existe una mutación en esa posición.
    # El número total de mutaciones.
    # El porcentaje de identidad entre ambas secuencias.

# Por ejemplo:
    # Secuencia 1: ATGCCGTA
    # Secuencia 2: ATGTCGAA

# Debería detectar diferencias como:
    # Posición 4: C → T
    # Posición 7: T → A

# Y terminar con algo tipo:
    # Mutaciones encontradas: 2
    # Identidad: 75.0%

import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6

def posicion_nucleotido(cadena):
    nucleotidos = cadena.split(" ")
    for indice, n in enumerate(nucleotidos):
        return f"Posición {indice+1} --> {n}"

if __name__ == "__main__":
    while True:
        sec_1 = input("Escribe la primera cadena de ADN: ").upper()
        sec_2 = input("Escribe la segunda cadena de ADN: ").upper()
        
        if p6.validar_secuencia(sec_1) and p6.validar_secuencia(sec_2):
            if len(sec_1) != len(sec_2):
                print("Ambas cadenas deben tener la misma longitud")
            else:
                print(posicion_nucleotido(sec_1))
                print(posicion_nucleotido(sec_2))
                break
        else:
            print("Secuencia de ADN incorrecta")
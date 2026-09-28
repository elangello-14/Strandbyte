import sys
from collections import Counter
from pathlib import Path
import Proyecto_11 as p11

# ------ ANALIZAR NUCLEÓTIDOS ------
def analizar_nucleotidos(secuencia):
    contador = Counter(secuencia)

    formula = 100 / len(secuencia)

    porcentaje = {
        'A': round(contador["A"] * formula, 2),
        'T': round(contador["T"] * formula, 2),
        'G': round(contador["G"] * formula, 2),
        'C': round(contador["C"] * formula, 2)
    }

    return porcentaje

print(analizar_nucleotidos("GATTACA"))

# ------ RESULTADOS -------
if __name__ == "__main__":
    try:
        archivo = input("Escribe la ruta del archivo fasta: ")
        fasta = p11.leer_fasta(Path(archivo))
    
    except FileNotFoundError:
        print("La ruta no es válida")
    
    else:
        pass
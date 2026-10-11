# Requisitos del proyecto
    # 1. Leer una secuencia de ADN desde un archivo FASTA reutilizando tu función leer_fasta() del Proyecto 11.
    # 2. Pedir al usuario el valor de \(k\), es decir, la longitud de los fragmentos.
    # 3. Generar todos los k-mers posibles de la secuencia.
    # 4. Contar cuántas veces aparece cada k-mer utilizando Counter.
    # 5. Mostrar los k-mers ordenados por frecuencia, de mayor a menor.
    # 6. Gestionar entradas incorrectas: por ejemplo, \(k \leq 0\), \(k\) mayor que la longitud de la secuencia o una secuencia vacía.

from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path

def mostrar_kmers(secuencia, k):
    kmers = [secuencia[i] for i in range(0, (len(secuencia)), k)]
    return kmers

if __name__ == "__main__":
    try:
        ruta = input("Escribe la ruta del archivo FASTA: ")
        fasta = leer_fasta(Path(ruta))
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
    else:
        k = int(input("Introduce la longitud de los kmers: "))
        secuencia = fasta["secuencia"]
        # mostrar_kmers(secuencia, k)
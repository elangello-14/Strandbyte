import sys
from collections import Counter
from pathlib import Path
import Proyecto_11 as p11

# ------ ANALIZAR NUCLEÓTIDOS ------
nucleotidos_globales = []

def analizar_nucleotidos(secuencia):
    contador = Counter(secuencia)
    formula = 100 / len(secuencia)

    porcentaje = {
        'A': round(contador["A"] * formula, 2),
        'T': round(contador["T"] * formula, 2),
        'G': round(contador["G"] * formula, 2),
        'C': round(contador["C"] * formula, 2)
    }

    return contador,porcentaje


def analizar_nucleotidos_globales(secuencia_global):
    contador = Counter(secuencia_global)
    formula = 100 / len(secuencia_global)

    porcentaje_global = {
        'A': round(contador["A"] * formula, 2),
        'T': round(contador["T"] * formula, 2),
        'G': round(contador["G"] * formula, 2),
        'C': round(contador["C"] * formula, 2)
    }

    return contador, porcentaje_global

# ------ RESULTADOS -------
if __name__ == "__main__":
    try:
        archivo = input("Escribe la ruta del archivo fasta: ")
        fasta = p11.leer_fasta(Path(archivo))
    
    except FileNotFoundError:
        print("La ruta no es válida")
    
    else:
        secuencias_globales = []
        for i in range (len(fasta)):
            secuencia = fasta[i]["secuencia"]
            secuencias_globales.append(secuencia)
            secuencia_global = ("").join(secuencias_globales)

            # ---- Resultado individual ----
            analisis = analizar_nucleotidos(secuencia)
            print(f'''
======= ANÁLISIS ========
Secuencia: {secuencia}

A --> {analisis[0]["A"]} ({analisis[1]["A"]}%)
T --> {analisis[0]["T"]} ({analisis[1]["T"]}%)
G --> {analisis[0]["G"]} ({analisis[1]["G"]}%)
C --> {analisis[0]["C"]} ({analisis[1]["C"]}%)
==========================
            ''')

        # ---- Resultado global -----
        analisis_global = analizar_nucleotidos_globales(secuencia_global)
        print(f'''
======= ANÁLISIS GLOBAL ========
Secuencia: {secuencia}

A --> {analisis_global[0]["A"]} ({analisis_global[1]["A"]}%)
T --> {analisis_global[0]["T"]} ({analisis_global[1]["T"]}%)
G --> {analisis_global[0]["G"]} ({analisis_global[1]["G"]}%)
C --> {analisis_global[0]["C"]} ({analisis_global[1]["C"]}%)
=================================
        ''')


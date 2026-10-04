from collections import Counter
from pathlib import Path
import Proyecto_11 as p11

# ------ ANALIZAR NUCLEÓTIDOS ------
def analizar_nucleotidos(secuencia, secuencia_global):
    contador = Counter(secuencia)
    contador_global = Counter(secuencia_global)

    formula = 100 / len(secuencia)
    formula_global = 100 / len(secuencia_global)

    porcentaje = {
        'A': round(contador["A"] * formula, 2),
        'T': round(contador["T"] * formula, 2),
        'G': round(contador["G"] * formula, 2),
        'C': round(contador["C"] * formula, 2)
    }

    porcentaje_global = {
        'A': round(contador_global["A"] * formula_global, 2),
        'T': round(contador_global["T"] * formula_global, 2),
        'G': round(contador_global["G"] * formula_global, 2),
        'C': round(contador_global["C"] * formula_global, 2)
    }

    datos = {
        "contador": contador,
        "contador_global": contador_global,
        "A": (porcentaje["A"], porcentaje_global["A"]),
        "T": (porcentaje["T"], porcentaje_global["T"]),
        "G": (porcentaje["G"], porcentaje_global["G"]),
        "C": (porcentaje["C"], porcentaje_global["C"])
    }

    return datos

# ------ RESULTADOS -------
if __name__ == "__main__":
    try:
        archivo = input("Escribe la ruta del archivo fasta: ")
        fasta = p11.leer_fasta(Path(archivo))
    
    except FileNotFoundError:
        print("La ruta no es válida")
    
    else:
        contenido = Path(archivo).read_text()
        if not contenido: print("El archivo está vacío")

        else:
            secuencias_globales = []
            for i in range (len(fasta)):
                secuencia = fasta[i]["secuencia"]
                secuencias_globales.append(secuencia)
                secuencia_global = ("").join(secuencias_globales)

                # ---- Resultado individual ----
                analisis = analizar_nucleotidos(secuencia, secuencia_global)
                print(f'''
======= ANÁLISIS ========
Secuencia: {secuencia}

A --> {analisis["contador"]["A"]} ({analisis["A"][0]}%)
T --> {analisis["contador"]["T"]} ({analisis["T"][0]}%)
G --> {analisis["contador"]["G"]} ({analisis["G"][0]}%)
C --> {analisis["contador"]["C"]} ({analisis["C"][0]}%)
==========================
                ''')

            # ---- Resultado global -----
            print(f'''
======= ANÁLISIS GLOBAL ========
Secuencia: {secuencia_global}
A --> {analisis["contador_global"]["A"]} ({analisis["A"][1]}%)
T --> {analisis["contador_global"]["T"]} ({analisis["T"][1]}%)
G --> {analisis["contador_global"]["G"]} ({analisis["G"][1]}%)
C --> {analisis["contador_global"]["C"]} ({analisis["C"][1]}%)
=================================
            ''')
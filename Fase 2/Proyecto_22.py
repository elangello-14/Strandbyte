from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path
import sys
sys.path.append("Fase 1")
from Proyecto_6 import validar_secuencia #type: ignore
import textwrap

# ----- FUNCIONES --------
def analisis_secuencia(secuencia):
    contador = Counter(secuencia)
    longitud = len(secuencia)
    
    formula = 100 / longitud
    gc = (contador["G"] + contador["C"]) * formula
    
    bases_ambiguas = {"N": contador["N"], "R": contador["R"], "Y": contador["Y"], "W": contador["W"], "S": contador["S"],}
    
    if bases_ambiguas:
        datos = {
        "secuencia": secuencia,
        "porcentaje_gc": round(gc, 2),
        "longitud": longitud,
        "bases": {"A": contador["A"], "T": contador["T"], "G": contador["G"], "C": contador["C"]},
        "bases_ambiguas": bases_ambiguas,
        "porcentaje_bases": {"A": round(contador["A"] * formula, 2), "T": round(contador["T"] * formula, 2), "G": round(contador["G"] * formula, 2), "C": round(contador["C"] * formula, 2)},
        "porcentaje_bases_ambiguas": {"N": round(contador["N"] * formula, 2), "R": round(contador["R"] * formula, 2), "Y": round(contador["Y"] * formula, 2), "W": round(contador["W"] * formula, 2), "S": round(contador["S"] * formula, 2)}
    }
    
    else: 
        datos = {
        "secuencia": secuencia,
        "porcentaje_gc": round(gc, 2),
        "longitud": longitud,
        "bases": {"A": contador["A"], "T": contador["T"], "G": contador["G"], "C": contador["C"]},
        "porcentaje_bases": {"A": round(contador["A"] * formula, 2), "T": round(contador["T"] * formula, 2), "G": round(contador["G"] * formula, 2), "C": round(contador["C"] * formula, 2)},
    }
    
    return datos


# ---- INPUTS Y RESULTADOS ----
if __name__ == "__main__":
    # ruta = input("Introduce la ruta del archivo FASTA: ")
    ruta = "Fase 2\\secuencias_2.fasta"
    archivo = Path(ruta)
    try:
        datos_fasta = leer_fasta(archivo)
    
    except FileNotFoundError:
        print("La ruta no es correcta")
    
    else:
        
        for i in range(len(datos_fasta)):
            secuencia = datos_fasta[i]["secuencia"]
            if not secuencia: print("No se ha encontrado la secuencia")
            
            if not validar_secuencia(secuencia):
                print("La secuencia es incorrecta")
                
            elif validar_secuencia(secuencia) == "True_chars_ambiguos":
                print(resultado)
                resultado_ambiguo = textwrap.dedent(f'''
                ------------------------------------                                    
                <<< Análisis ambiguo >>>
                Secuencia: {analisis["secuencia"]}
                    - Longitud: {analisis["longitud"]} nt
                    - GC%: {analisis["porcentaje_gc"]}%
                    - Conteo de bases:
                        A: {analisis["bases"]["A"]} ({analisis["porcentaje_bases"]["A"]}%)
                        T: {analisis["bases"]["T"]} ({analisis["porcentaje_bases"]["T"]}%)
                        G: {analisis["bases"]["G"]} ({analisis["porcentaje_bases"]["G"]}%)
                        C: {analisis["bases"]["C"]} ({analisis["porcentaje_bases"]["C"]}%)
                        N: {analisis["bases_ambiguas"]["N"]} ({analisis["porcentaje_bases_ambiguas"]["A"]}%)
                        R: {analisis["bases_ambiguas"]["R"]} ({analisis["porcentaje_bases_ambiguas"]["T"]}%)
                        Y: {analisis["bases_ambiguas"]["Y"]} ({analisis["porcentaje_bases_ambiguas"]["G"]}%)
                        W: {analisis["bases_ambiguas"]["W"]} ({analisis["porcentaje_bases_ambiguas"]["C"]}%)
                        S: {analisis["bases_ambiguas"]["S"]} ({analisis["porcentaje_bases_ambiguas"]["C"]}%)
                ''')
            
            else:
                analisis = analisis_secuencia(secuencia)
                resultado = textwrap.dedent(f'''
                ------------------------------------
                Secuencia: {analisis["secuencia"]}
                    - Longitud: {analisis["longitud"]} nt
                    - GC%: {analisis["porcentaje_gc"]}%
                    - Conteo de bases:
                        A: {analisis["bases"]["A"]} ({analisis["porcentaje_bases"]["A"]}%)
                        T: {analisis["bases"]["T"]} ({analisis["porcentaje_bases"]["T"]}%)
                        G: {analisis["bases"]["G"]} ({analisis["porcentaje_bases"]["G"]}%)
                        C: {analisis["bases"]["C"]} ({analisis["porcentaje_bases"]["C"]}%)
                ''')
                print(resultado)
                print("-----------------------------")
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
                
            elif validar_secuencia == "True_chars_ambiguos":
                print(resultado)
                resultado_ambiguo = textwrap.dedent(f'''
                Análisis ambiguo
                
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
from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path
import sys
sys.path.append("Fase 1")
from Proyecto_6 import validar_secuencia #type: ignore

# ----- FUNCIONES --------
def analisis_secuencia(secuencia):
    contador = Counter(secuencia)
    longitud = len(secuencia)
    
    formula = 100 / longitud
    gc = (contador["G"] + contador["C"]) * formula
    
    
    datos = {
        "secuencia": secuencia,
        "porcentaje_gc": round(gc, 2),
        "longitud": longitud,
        "bases": {"A": contador["A"], "T": contador["T"], "G": contador["G"], "C": contador["C"]}, # ¿redundante con Counter(secuencia)?
        "porcentaje_bases": {"A": round(contador["A"] * formula, 2), "T": round(contador["T"] * formula, 2), "G": round(contador["G"] * formula, 2), "C": round(contador["C"] * formula, 2)}
    }
    
    return datos


# ---- INPUTS Y RESULTADOS ----
if __name__ == "__main__":
    try:
        ruta = input("Introduce la ruta del archivo FASTA: ")
        # ruta = "Fase 2\\secuencias.fasta"
        archivo = Path(ruta)
    
    except FileNotFoundError:
        print("La ruta no es correcta")
    
    else:
        datos_fasta = leer_fasta(archivo)

        
        for i in range(len(datos_fasta)):
            secuencia = datos_fasta[i]["secuencia"]
            
            if not validar_secuencia(secuencia):
                print("La secuencia es incorrecta")
            
            else:
                secuencias = []
                secuencias.append(secuencia)

                for secuencia in secuencias:
                    analisis = analisis_secuencia(secuencia)
                    resultado = f'''
                    ------------------------------------
                    Secuencia: {analisis["secuencia"]}

                        - Longitud: {analisis["longitud"]} pb

                        - GC%: {analisis["porcentaje_gc"]}%

                        - Conteo de bases:
                            A: {analisis["bases"]["A"]} ({analisis["porcentaje_bases"]["A"]}%)
                            T: {analisis["bases"]["T"]} ({analisis["porcentaje_bases"]["T"]}%)
                            G: {analisis["bases"]["G"]} ({analisis["porcentaje_bases"]["G"]}%)
                            C: {analisis["bases"]["C"]} ({analisis["porcentaje_bases"]["C"]}%)
                    ------------------------------------
                    '''

                    print(resultado) # en el resultado, ¿se puede borrar los espacios en blanco a la izquierda para que. en la consola, el margen quede correcto sin modificar la identación del código usando las triples comillas? Porque si cambio la identación, entonces el código se ve peor y más ilegible, pero tampoco quiero llenar cada línea de prints.
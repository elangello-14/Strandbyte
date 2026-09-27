import sys
from pathlib import Path
sys.path.append("Fase 1")
import Proyecto_6 as p6 # type: ignore
import Proyecto_11 as p11
import Proyecto_16 as p16

# ------ FUNCIÓN MOSTRAR RESULTADO --------
def mostrar_resultado(referencia, muestra, i, resultado, resultados):
    return f'''
-------------------------------------
Secuencia de referencia: {referencia}
Secuencia de muestra {i+1}: {muestra}

Mutaciones: {" ".join(resultado["mutaciones"])}
Cantidad de mutaciones: {resultado["cantidad_mutaciones"]}

Identidad: {resultado["identidad"]}

Secuencia con más mutaciones: {(max(resultados, key=lambda resultado: resultado["cantidad_mutaciones"]))["cadena"]}
Secuencia con menos mutaciones: {(min(resultados, key=lambda resultado: resultado["cantidad_mutaciones"]))["cadena"]}
-------------------------------------

'''

# ----- RESULTADOS -------
if __name__ == "__main__":
    referencia = input("Escribe una secuencia de referencia: ").upper()
    
    if p6.validar_secuencia(referencia):
        try:
            archivo = input("Escribe la ruta del archivo fasta: ")
            fasta = p11.leer_fasta(Path(archivo))
        
        except FileNotFoundError:
            print("La ruta no es válida")
        
        else:
            secuencias_fasta = []
            for i in range(0, len(fasta)):
                secuencia_fasta = fasta[i]["secuencia"]
                secuencias_fasta.append(secuencia_fasta)
            
            resultados = []
            for muestra in secuencias_fasta:
                resultado = p16.comparar_secuencias(referencia, muestra)
                resultados.append(resultado)
                print(mostrar_resultado(referencia, muestra, i, resultado, resultados))
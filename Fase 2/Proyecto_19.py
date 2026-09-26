import sys
from pathlib import Path
sys.path.append("Fase 1")
import Proyecto_6 as p6 # type: ignore
import Proyecto_11 as p11
import Proyecto_16 as p16

# ----- RESULTADOS -------
if __name__ == "__main__":
    referencia = input("Escribe una secuencia de referencia: ").upper()
    
    if p6.validar_secuencia(referencia):
        archivo = input("Escribe la ruta del archivo fasta: ")
        fasta = p11.leer_fasta(Path(archivo))
        
        secuencias_fasta = []
        for i in range(0, len(fasta)):
            secuencia_fasta = fasta[i]["secuencia"]
            secuencias_fasta.append(secuencia_fasta)
        
        for muestra in secuencias_fasta:
            resultado = p16.comparar_secuencias(referencia, muestra)
            print(resultado)
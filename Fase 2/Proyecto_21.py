from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path
import sys
sys.path.append("Fase 1")
from Proyecto_6 import validar_secuencia # type: ignore

# ------ Función mostrar kmers --------
def mostrar_kmers(secuencia, k):
    if k <= 0 or k > len(secuencia):
        return None
    
    else:
        kmers = [secuencia[i: i+k] for i in range(0, (len(secuencia) - k + 1), 1)]

        contador = Counter(kmers)

        kmers_ordenados = contador.most_common()
        
        datos = []
        for i in range(len(kmers_ordenados)):
            resultado = f"{kmers_ordenados[i][0]} ---> {kmers_ordenados[i][1]}\n"
            datos.append(resultado)

        return datos


# ------- Inputs y resultados --------------
if __name__ == "__main__":
    try:
        ruta = input("Escribe la ruta del archivo FASTA: ")
        fasta = leer_fasta(Path(ruta))
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
    else:
        try:
            k = int(input("Introduce la longitud de los kmers: "))
        except ValueError:
            print("Escribe una longitud correcta")
            
        else:
            for i in range(len(fasta)):
                secuencia = fasta[i]["secuencia"]
                
                if not validar_secuencia(secuencia):
                    print("Secuencia incorrecta. No se ha podido analizar\n")
                
                else:
                    resultado = mostrar_kmers(secuencia, k)
                    if not resultado:
                        print("Escribe una longitud válida")
                
                    else:
                        print(" ".join(resultado))
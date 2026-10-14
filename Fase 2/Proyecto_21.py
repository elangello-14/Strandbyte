from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path
import sys
sys.path.append("Fase 1")
from Proyecto_6 import validar_secuencia # type: ignore

# ------ Función mostrar kmers --------
def mostrar_kmers(secuencia, k):
    if k <= 1 or k >= len(secuencia):
        return None
    
    else:
        kmers = [secuencia[i: i+k] for i in range(0, (len(secuencia)), k)]

        if len(kmers[-1]) != k:
            del kmers[-1]

        contador = Counter(kmers)

        kmers_contados = []
        for kmer in kmers:
            kmers_contados.append(contador[kmer])

        kmers_contados_ordenados = sorted(kmers_contados, reverse=True)
        kmers_ordenados = sorted(kmers, reverse=True, key=lambda x: contador[x])
        kmers_ordenados = list(set(kmers_ordenados))

        datos = []
        for i in range(len(kmers_ordenados)):
            resultado = f"{kmers_ordenados[i]} ---> {kmers_contados_ordenados[i]}\n"
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
        except:
            print("Escribe una longitud correcta")
            
        else:
            for i in range(len(fasta)):
                secuencia = fasta[i]["secuencia"]
                resultado = mostrar_kmers(secuencia, k)
                
                if not validar_secuencia(secuencia):
                    print("Secuencia incorrecta. No se ha podido analizar\n")
                
                else:
                    if not resultado:
                        print("Escribe una longitud válida")
                        break
                
                    else:
                        print(" ".join(resultado))
# Verificar para 17/10

from Proyecto_11 import leer_fasta
from collections import Counter
from pathlib import Path

def mostrar_kmers(secuencia, k):
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
    
    for i in range(len(kmers_ordenados)):
        print(f"{kmers_ordenados[i]} ---> {kmers_contados_ordenados[i]}")

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
            try:
                for i in range(len(fasta)):
                    secuencia = fasta[i]["secuencia"]
                    print("\n-------------------------")
                    mostrar_kmers(secuencia, k)
            except:
                print("Escribe una longitud correcta")     
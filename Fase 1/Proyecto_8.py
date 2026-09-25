import Proyecto_1 as p1
import Proyecto_2 as p2

with open("Fase 1\proyecto_8.txt", encoding="UTF-8") as archivo:
    secuencias = archivo.readlines()
    if __name__ == "__main__":
        for indice, cadena in enumerate(secuencias):
            cadena = cadena.strip()
        
            print(f'''
Secuencia {indice + 1}: {cadena}
Longitud: {p1.longitud_secuencia(cadena)}
Porcentaje GC: {p2.calculadora_GC(cadena)}%
    ''')
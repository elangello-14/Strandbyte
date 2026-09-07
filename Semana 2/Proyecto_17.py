import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore

def analizar_secuencia(cadena):
    longitud = len(cadena)
    gc = ((cadena.count("G") + cadena.count("C")))
    at = ((cadena.count("A") + cadena.count("T")))
    secuencia_larga = max(secuencias, key=len(secuencia))
    secuencia_gc = max(secuencias, key=secuencia.count("G"), key=secuencia.count("C")) 
    
    datos = {
        "secuencia": cadena,
        "longitud": longitud,
        "GC": gc,
        "AT": at,
        "secuencia_larga": secuencia_larga,
        "secuencia_gc": secuencia_gc

    }

body_informe = f'''
Secuencia:
Longitud:
GC:
AT:

--------------------

Secuencia más larga: 
Secuencia con mayor GC:
Longitud media:

--------------------

Secuencia con menor GC:
Secuencia más corta:
'''


if __name__ == "__main__":
    secuencias = []
    
    while True:
        for secuencia in secuencias:
            secuencia = input("Introduce secuencias de ADN para hacer un informe\nEscribe 'continuar' para obtener el informe: ").upper()
            if p6.validar_secuencia(secuencia) and secuencia != "CONTINUAR":
                secuencias.append(secuencia)
                print("\nSecuencia añadida!")
            else:
                print("\n La secuencia es inválida")

            if secuencia == "CONTINUAR":
                pass
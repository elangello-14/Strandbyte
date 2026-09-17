import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore

# Funciones
def analizar_secuencia(cadena):
    longitud = len(cadena)
    longitudes.append(longitud)
    gc = ((cadena.count("G") + cadena.count("C")) * 100) / len(cadena)
    at = ((cadena.count("A") + cadena.count("T")) * 100) / len(cadena)
    return cadena, longitud, gc, at

def resumen_secuencias(cadena):
    secuencia_larga = max(secuencias, key=len)
    secuencia_mayor_gc = max(secuencias, key=lambda x: x.count("G") + x.count("C"))
    longitud_media = round(sum(longitudes) / len(longitudes), 1)
    secuencia_menor_gc = min(secuencias, key=lambda x: x.count("G") + x.count("C"))
    secuencia_corta = min(secuencias, key=len)

def mostrar_informe():
    datos = {
        "secuencia": analizar_secuencia[0],
        "longitud": analizar_secuencia[1],
        "GC": f"{round(analizar_secuencia[2], 2)}%",
        "AT": f"{round(analizar_secuencia[3], 2)}%",
        # "secuencia_larga": resumen_secuencias.secuencia_larga(cadena),
        # "secuencia_mayor_gc": resumen_secuencias.secuencia_mayor_gc(cadena),
        # "longitud_media": f"{resumen_secuencias.longitud_media(cadena)} nucleótidos",
        # "secuencia_menor_gc": resumen_secuencias.secuencia_menor_gc(cadena),
        # "secuencia_corta": resumen_secuencias.secuencia_corta(cadena)
    }   
    body_informe = f'''--------------------------------
Secuencia: {datos["secuencia"]}
Longitud: {datos["longitud"]}
GC: {datos["GC"]}
AT: {datos["AT"]}


'''
    return body_informe

secuencias = []
longitudes = []

# Interacción Usuario <-> Sistema
if __name__ == "__main__":
    while True:
        secuencia_adn = input("Introduce secuencias de ADN para hacer un informe\nEscribe 'continuar' para obtener el informe: ").upper()

        if p6.validar_secuencia(secuencia_adn) and secuencia_adn != "CONTINUAR":
            secuencias.append(secuencia_adn)
            print("\n---> Secuencia añadida!")
        elif secuencia_adn == "CONTINUAR":
            for indice, secuencia in enumerate(secuencias):
                print(f"\n///////// INFORME nº {indice + 1} /////////")
                print(mostrar_informe())
            break
        else:
            print("\n---> La secuencia es inválida")
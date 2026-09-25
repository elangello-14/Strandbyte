import sys
sys.path.append("Fase 1")
import Proyecto_6 as p6 # type: ignore

# Funciones
def analizar_secuencia(cadena):
    longitud = len(cadena)
    gc = ((cadena.count("G") + cadena.count("C")) * 100) / len(cadena)
    at = ((cadena.count("A") + cadena.count("T")) * 100) / len(cadena)
    return cadena, longitud, gc, at

def resumen_secuencias(cadena):
    longitudes.append(analizar_secuencia(cadena)[1])
    secuencia_larga = max(secuencias, key=len)
    secuencia_mayor_gc = max(secuencias, key=lambda x: x.count("G") + x.count("C"))
    longitud_media = round(sum(longitudes) / len(longitudes), 1)
    secuencia_menor_gc = min(secuencias, key=lambda x: x.count("G") + x.count("C"))
    secuencia_corta = min(secuencias, key=len)
    return secuencia_larga, secuencia_mayor_gc, longitud_media, secuencia_menor_gc, secuencia_corta, longitudes

def mostrar_informe(cadena):
    datos_secuencia = analizar_secuencia(cadena)
    datos_resumen_secuencia = resumen_secuencias(cadena)
    datos = {
        "secuencia": datos_secuencia[0],
        "longitud": datos_secuencia[1],
        "GC": f"{round(datos_secuencia[2], 2)}%",
        "AT": f"{round(datos_secuencia[3], 2)}%",
        "secuencia_larga": datos_resumen_secuencia[0],
        "secuencia_mayor_gc": datos_resumen_secuencia[1],
        "longitud_media": f"{datos_resumen_secuencia[2]} nucleótidos",
        "secuencia_menor_gc": datos_resumen_secuencia[3],
        "secuencia_corta": datos_resumen_secuencia[4]
    }
    
    body_informe = f'''Secuencia: {datos["secuencia"]}
Longitud: {datos["longitud"]}
GC: {datos["GC"]}
AT: {datos["AT"]}

--------------------------------
Secuencia más larga: {datos["secuencia_larga"]}
Secuencia con más GC: {datos["secuencia_mayor_gc"]}
Longitud media: {datos["longitud_media"]}

--------------------------------
Secuencia más corta: {datos["secuencia_corta"]}
Secuencia con menos GC: {datos["secuencia_menor_gc"]}\n
/////////////////////////////////
{datos_resumen_secuencia[5]}

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
                print(mostrar_informe(secuencia))
            break
        else:
            print("\n---> La secuencia es inválida")
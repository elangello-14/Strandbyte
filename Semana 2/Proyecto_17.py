import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore

def analizar_secuencia(cadena):
    longitud = len(cadena)
    longitudes.append(longitud)
    gc = ((cadena.count("G") + cadena.count("C")))
    at = ((cadena.count("A") + cadena.count("T")))
    secuencia_larga = max(secuencias, key=len)
    secuencia_mayor_gc = max(secuencias, key=lambda x: x.count("G") and x.count("C"))
    longitud_media = round(sum(longitudes) / len(longitudes), 1)
    secuencia_menor_gc = min(secuencias, key=lambda x: x.count("G") and x.count("C"))
    secuencia_corta = min(secuencias, key=len)

        
    datos = {
        "secuencia": cadena,
        "longitud": longitud,
        "GC": gc,
        "AT": at,
        "secuencia_larga": secuencia_larga,
        "secuencia_mayor_gc": secuencia_mayor_gc,
        "longitud_media": f"{longitud_media} nucleótidos",
        "secuencia_menor_gc": secuencia_menor_gc,
        "secuencia_corta": secuencia_corta
    }

    body_informe = f'''--------------------------------
Secuencia: {datos["secuencia"]}
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

'''
    return body_informe


if __name__ == "__main__":
    secuencias = []
    longitudes = []

    while True:
        secuencia_adn = input("Introduce secuencias de ADN para hacer un informe\nEscribe 'continuar' para obtener el informe: ").upper()

        if p6.validar_secuencia(secuencia_adn) and secuencia_adn != "CONTINUAR":
            secuencias.append(secuencia_adn)
            print("\n---> Secuencia añadida!")
        elif secuencia_adn == "CONTINUAR":
            for indice, secuencia in enumerate(secuencias):
                print(f"\n///////// INFORME nº {indice + 1} /////////")
                print(analizar_secuencia(secuencia))
            break
        else:
            print("\n---> La secuencia es inválida")
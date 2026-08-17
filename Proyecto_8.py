

with open("proyecto_8.txt", encoding="UTF-8") as archivo:
    secuencias = archivo.readlines()
    longitud = len(secuencias)
    
    for cadena in secuencias:
        
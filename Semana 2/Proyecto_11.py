from pathlib import Path

archivo = Path("Semana 2\\secuencias.fasta")
lineas = archivo.read_text().splitlines()

datos = [
    
]

secuencia_actual = 0

secuencias = []

for linea in lineas:
    if linea.startswith(">"):
        
        nombre = linea.split(" ")[0].removeprefix(">")
        
        descripcion = linea.split(" ")[1:200]
        descripcion = " ".join(descripcion)
        
        insertar = {
            "nombre": nombre,
            "descripcion": descripcion,
            "secuencia": ""
            }
        
        datos.append(insertar)
        
        secuencia_actual += 1
        
    else:
        secuencias.append(linea.split(" "))
        
        for i in range(0, len(secuencias)):
            secuencia_actual = datos[-1]
            secuencia_actual["secuencia"].join(secuencias[i])
    
print(secuencias)
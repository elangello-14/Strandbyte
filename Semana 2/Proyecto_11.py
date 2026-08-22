from pathlib import Path

archivo = Path("Semana 2\\secuencias.fasta")
lineas = archivo.read_text().splitlines()

datos = [
    
]

for linea in lineas:
    if linea.startswith(">"):
        secuencia_actual = 0
        secuencia_actual += 1
        
        nombre = linea.split(" ")[0].removeprefix(">")
        
        descripcion = linea.split(" ")[1:200]
        descripcion = " ".join(descripcion)
        
        insertar = {
            "nombre": nombre,
            "descripcion": descripcion
            }
        
        datos.append(insertar)
        
    else:
        print(linea.split(" "))
        while secuencia_actual

print(datos)
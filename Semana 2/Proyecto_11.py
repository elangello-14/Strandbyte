from pathlib import Path

archivo = Path("Semana 2\\secuencias.fasta")
lineas = archivo.read_text().splitlines()
print(lineas)

for linea in lineas:
    if linea.startswith(">"):
        nombre = linea.split(" ")[0].removeprefix(">")
        
        descripcion = linea.split(" ")[1:200]
        descripcion = " ".join(descripcion)
        
        datos = {
            "nombre": f"{nombre}",
            "descripcion": f"{descripcion}"
        }
        print(datos["descripcion"])

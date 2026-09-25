from pathlib import Path

archivo = Path("Fase 2\\secuencias.fasta")
lineas = archivo.read_text().splitlines()

datos = [
    
]

secuencias = []

for linea in lineas:
    if linea.startswith(">"):
        nombre = linea.split(" ")[0].removeprefix(">")
        
        descripcion = linea.split(" ")[1:200]
        descripcion = " ".join(descripcion)
        
        insertar = {
            "nombre": nombre,
            "descripcion": descripcion,
            "secuencia": "",
            "longitud": ""
            }
        
        datos.append(insertar)

    else:
        secuencia = datos[-1]
        secuencia["secuencia"] += linea
        secuencia["longitud"] = f"{len(linea)} pb"

if __name__ == "__main__":
    for i in range(len(datos)):
        print(f'''
Nombre: {datos[i]["nombre"]}
Descripción: {datos[i]["descripcion"]}
Secuencia: {datos[i]["secuencia"]}
Longitud: {datos[i]["longitud"]}
''')
from pathlib import Path

# ---- LEER ARCHIVO FASTA ----
def leer_fasta(archivo):
    lineas = archivo.read_text().splitlines()
    
    datos = [
    
    ]
    
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
        
    return datos

# ------- RESULTADOS ---------
if __name__ == "__main__":
    resultado = leer_fasta(Path("Fase 2\\secuencias.fasta"))
    for i in range(len(resultado)):
        
        print(f'''
Nombre: {resultado[i]["nombre"]}
Descripción: {resultado[i]["descripcion"]}
Secuencia: {resultado[i]["secuencia"]}
Longitud: {resultado[i]["longitud"]}
''')
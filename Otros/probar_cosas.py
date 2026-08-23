datos = []  # lista vacía

# Simulamos leer una cabecera
datos.append({"nombre": "seq_1", "descripcion": "Insulina", "secuencia": ""})

# Ahora "apuntamos" al último diccionario
secuencia_actual = datos[-1]

# Simulamos leer una línea de ADN
secuencia_actual["secuencia"] += "ATGGCC"

# Simulamos leer otra línea de ADN
secuencia_actual["secuencia"] += "CTGTGG"

print(datos)


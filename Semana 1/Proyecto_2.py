import Proyecto_1 as p1

# Funcionalidades
def calculadora_GC(cadena):
    porcentaje = (cadena.count("G") + cadena.count("C")) * 100 / p1.longitud_secuencia(cadena)
    return round(porcentaje, 2)

# Inputs y resultados
if __name__ == "__main__":
    secuencia = input("Escribe la secuencia de ADN: ")
    secuencia = secuencia.upper()
    print(f"El porcentaje GC es {calculadora_GC(secuencia)}%")


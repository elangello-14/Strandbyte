# Funcionalidades
def buscar_mutaciones(cadena_1, cadena_2):
    for posicion, (nucleotido_c1, nucleotido_c2) in enumerate(zip(cadena_1, cadena_2)):
        if nucleotido_c1 != nucleotido_c2:
            print(f'''
Mutación en posicion {posicion + 1}
{nucleotido_c1} --> {nucleotido_c2}
''')

# Inputs y resultados
if __name__ == "__main__":
    print("//// BUSCADOR DE MUTACIONES ////")
    secuencia_1 = input("Introduce la primera cadena: ")
    secuencia_2 = input("Introduce la segunda cadena: ")
    
    if secuencia_1 == secuencia_2:
        print("No existen mutaciones")
    else:
        buscar_mutaciones(secuencia_1, secuencia_2)








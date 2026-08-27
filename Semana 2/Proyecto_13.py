# Fragmento de código sacado del Proyecto 10
menu = '''
=== DNA Toolkit ===

1 Analizar ADN

2 Calcular GC

3 Complementaria

4 Reverse Complement

5 Salir
'''

if __name__ == "__main__":
    print(menu)

    while True:
        try:
            menu_opcion = int(input("Introduce una opción (1 - 5): "))
            if menu_opcion < 5 and menu_opcion > 0:
                print("Funcionalidad X")
            elif menu_opcion == 5:
                print("Saliendo...")
                break
            else:
                print("Escribe una opción válida")
        except:
            print("Escribe una opción válida")
import Proyecto_1 as p1
import Proyecto_2 as p2
import Proyecto_3 as p3
import Proyecto_4 as p4
import Proyecto_6 as p6
import Proyecto_7 as p7
import Proyecto_9 as p9

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
        menu_opcion = input("Introduce una opción (1 - 5): ")
        if menu_opcion.isdigit() == False: print("Opción inválida. Escribe una opción del 1 al 5")
        else:
            menu_opcion = int(menu_opcion)
            if menu_opcion >= 1 and menu_opcion < 5:
        
                secuencia = input("Escribe la secuencia de ADN: ")
                secuencia = secuencia.upper()
                
                if p6.validar_secuencia(secuencia):
                    print("Secuencia de ADN correcta!")
                    
                    if menu_opcion == 1:
                        print(f"Longitud: {p1.longitud_secuencia(secuencia)}")
                        print(p1.conteo_secuencia(secuencia))
                        print(f"Base más frecuente: {p7.base_mas_frecuente(secuencia)}")
                        print(f"Cadena ARN: {p9.traducir_a_ARN(secuencia)}")
                        
                                
                    elif menu_opcion == 2:
                        print(f"Porcentaje GC: {p2.calculadora_GC(secuencia)}%")
                                
                    elif menu_opcion == 3:
                        print(f"Cadena complemetaria: {p3.cadena_complementaria(secuencia)}")
                            
                    elif menu_opcion == 4:
                        print(f"Cadena complementaria inversa: {p4.cadena_complementaria_inversa(secuencia)}")
                    
                else:
                    print("Secuencia de ADN incorrecta")
            elif menu_opcion == 5: break
            else: print("Opción inválida")
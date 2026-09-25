import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore
import Proyecto_16 as p16

# Inputs y resultados
if __name__ == "__main__":
    secuencias_de_muestra = []

    while True:
        secuencia_referencia = input("Escribe una secuencia de referencia: ").upper()

        if p6.validar_secuencia(secuencia_referencia):
            print("\nAhora, escribe tantas secuencias de muestra como quieras. Escribe 'N' para continuar cuando hayas finalizado")
            while True:
                secuencia_muestra = input(f"---> Muestra {len(secuencias_de_muestra) + 1}: ").upper()
    
                if p6.validar_secuencia(secuencia_muestra) and len(secuencia_referencia) == len(secuencia_muestra):
                    secuencias_de_muestra.append(secuencia_muestra)
                
                elif secuencia_muestra == "N": 
                    if not secuencias_de_muestra:
                        print("Debes introducir al menos una secuencia de muestra")
                    else:
                        resultados = []

                        for i, secuencia in enumerate(secuencias_de_muestra):
                            resultado = p16.comparar_secuencias(secuencia_referencia, secuencias_de_muestra)
                            resultados.append(resultado)
                            print(resultados)
                            # print("\n----------------------------------------------")
                            # print(f"Secuencia de referencia: {secuencia_referencia}")
                            # print(f"Muestra {i+1}: {secuencia}")
                            # print(f'\n---> Cantidad de mutaciones: {resultado["cantidad_mutaciones"]}')
                            # print(f'\n---> Mutaciones:\n{" ".join(resultado["mutaciones"])}')
                            # print(f'\n---> Identidad: {resultado["identidad"]}')
                            # print(f'\n---> Secuencia con más mutaciones: {max(resultados, key=lambda x: resultado[x])}')
                            # print("----------------------------------------------\n")
                    break
                
                else:
                    print("La secuencia es inválida o no tiene la misma longitud que la secuencia de referencia")
            break
        else:
            print("La secuecia es inválida")
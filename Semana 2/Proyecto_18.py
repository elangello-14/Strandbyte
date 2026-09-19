import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore
import Proyecto_16 as p16

# Inputs y resultados
secuencias_de_muestra = []
indice = 0
if __name__ == "__main__":
    while True:
        secuencia_referencia = input("Escribe una secuencia de referencia: ").upper()

        if p6.validar_secuencia(secuencia_referencia):
            print("\nAhora, escribe tantas secuencias de muestra como quieras. Escribe 'N' para continuar cuando hayas finalizado")
            while True:
                indice += 1
                secuencia_muestra = input(f"---> Muestra {indice}: ").upper()
    
                if p6.validar_secuencia(secuencia_muestra) and len(secuencia_referencia) == len(secuencia_muestra):
                    secuencias_de_muestra.append(secuencia_muestra)
                elif secuencia_muestra == "N": 
                    for i, secuencia in enumerate(secuencias_de_muestra):
                        print("\n----------------------------------------------")
                        print(f"Secuencia de referencia: {secuencia_referencia}")
                        print(f"Muestra {i+1}: {secuencia}")
                        p16.comparar_secuencias(secuencia_referencia, secuencia)
                        print("----------------------------------------------\n")
                    break
                else:
                    indice -= 1
                    print("La secuencia es inválida o no tiene la misma longitud que la secuencia de referencia")
            break
        else:
            print("La secuecia es inválida")
import sys
sys.path.append("Semana 1")
import Proyecto_6 as p6 # type: ignore

def comparar_secuencias(cadena_1, cadena_2):
    identidad = len(cadena_1)
    mutaciones = []
    
    for indice, (nucleotidos_1, nucleotidos_2) in enumerate(zip(cadena_1, cadena_2)):
        if nucleotidos_1 != nucleotidos_2:
            mutaciones.append(f"Posición {indice + 1}: {nucleotidos_1} → {nucleotidos_2}")
            identidad -= 1
    
    if not mutaciones:
        print("\nNo se han encontrado mutaciones")
    
    datos = {
        "mutaciones": mutaciones,
        "cantidad_mutaciones": len(mutaciones),
        "identidad": f"{round((identidad * 100)/len(cadena_1), 2)}%"
        }
    
    return datos

if __name__ == "__main__":
    while True:
        sec_1 = input("Escribe la primera cadena de ADN: ").upper()
        sec_2 = input("Escribe la segunda cadena de ADN: ").upper()
        
        if p6.validar_secuencia(sec_1) and p6.validar_secuencia(sec_2):
            if len(sec_1) != len(sec_2):
                print("Ambas cadenas deben tener la misma longitud")
            else:
                print(comparar_secuencias(sec_1, sec_2))
                break
        else:
            print("Secuencia de ADN incorrecta")
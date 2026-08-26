import sys
sys.path.append("C:\\Users\\usuario\\Documents\\Python - Mini proyectos de bioinformática\\Semana 1")
import Proyecto_6 as p6

#Funcionalidades
codificacion = {
    "ATG": "M",
    "GCC": "A",
    "CTG": "L",
}

proteina = []

# Inputs y resultados
if __name__ == "__main__":
    while True:
        secuencia_adn = input("Escribe la secuencia de ADN: ")
        secuencia_adn = secuencia_adn.upper()

        if p6.validar_secuencia(secuencia_adn):
            if len(secuencia_adn) % 3 != 0:
                print("AVISO: La longitud de la secuencia introducida no es óptima para la traducción a proteína. La longitud debe ser múltiplo de 3")

            for i in range(0, len(secuencia_adn), 3):
                codones = secuencia_adn[i: i+3]

                if codones in codificacion:
                    proteina.append(codificacion[codones])
            if proteina == [] : 
                print("----> No se han encontrado codones para formar una proteína")
            else:
                print(f"----> La proteína formada es: {"".join(proteina)}")
            break

        else:
            print("Secuencia de ADN inválida")
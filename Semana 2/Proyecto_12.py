import sys
sys.path.append("C:\\Users\\usuario\\Documents\\Python - Mini proyectos de bioinformática\\Semana 1")
sys.path.append("C:\\Users\\usuario\\Documents\\Python - Mini proyectos de bioinformática\\Semana 1")
import Proyecto_9 as p9
import Proyecto_6 as p6


# Inputs y resultados
secuencia_adn = input("Escribe la secuencia de ADN: ")
secuencia_adn = secuencia_adn.upper()

#Funcionalidades

codones_relevantes = ["AUG", "UUU", "CCC", "UAA", "UAG", "UGA"]

codificacion = {
    "AUG": "Metionina (Inicio)",
    "UUU": "Fenilanina",
    "CCC": "Prolina",
    ("UAA", "UAG", "UGA"): "Parada (STOP)"
}


while True:
    if p6.validar_secuencia(secuencia_adn) == True:
        secuencia_arn = p9.traducir_a_ARN(secuencia_adn)

        codon = [secuencia_arn[i:i+3] for i in range(0, len(secuencia_arn), 3)]

        for i in range(0, len(codones_relevantes)):
            if codones_relevantes[i] in codon:
                print("pito")
        break
    else:
        print("Secuencia de ADN inválida")

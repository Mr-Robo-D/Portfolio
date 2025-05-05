#NOME: DANILO PEREIRA DE LIMA
#RA: 2571392222015
# Avaliação 1 - Processamento de Linguagem Natural

import re

def remove_girias(texto):

    correcao = {"vc": "você ", "eh": "é", "mt": " muito ", "mto": " muito ", "dmr":"demorou","tmj":"estamos juntos","tb":"também","tbm":"também"}
    texto = "Vc eh mt bom, recomendo mto !!!"
    texto_dividido = re.findall(r'\b[\w]+|[^\s\w]', texto.lower())
    novo_texto = " "

    for elemento in texto_dividido:
        if elemento in correcao:
            novo_texto += correcao[elemento]
        else:
            novo_texto += elemento


    return novo_texto


texto_exemplo = "Vc eh mt bom, recomendo mto!!!"

print(remove_girias(texto_exemplo))
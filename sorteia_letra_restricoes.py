import random

def sorteia_letra(pais, letras_restritas):

    caracteres_especiais = ['.', ',', '-', ';', ' '] # lista de caracteres especiais

    # checando se o pais tem alguma letra que pode ser sorteada (se nao vai devolver uma string vazia)
    letra_valida = False
    for letra in pais:

        if letra.lower() not in letras_restritas and letra not in caracteres_especiais: 

            letra_valida = True

            break

    if letra_valida == False:

        return ""

    # sorteando a letra:
    continua = True
    pais_soletrado = []
    while continua:
        for letra in pais:
            pais_soletrado.append(letra.lower())
        letra = random.choice(pais_soletrado)

        if letra.lower() not in letras_restritas and letra not in caracteres_especiais:

            return letra
            
print(sorteia_letra("Andorra a-Velha", ['a', 'r']))
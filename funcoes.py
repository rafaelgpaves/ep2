from math import *
from random import *

def adiciona_em_ordem(nome_pais, d, paises):

    if nome_pais in paises:

        return paises

    distancias = [d] #lista de distancias

    for pais in paises:

        distancias.append(pais[1])

    distancias.sort() #arruamndo as distancias em ordem crescente
    i = distancias.index(d) #indice da distancia desse pais
    paises.insert(i, [nome_pais, d])

    return paises

###

def haversine(raio, lat1, long1, lat2, long2):
    calc_raio = 2 * raio
    calc_lat = ((lat2) - (lat1)) / 2
    calc_long = (long2 - long1) / 2
    parenteses = (sin(radians(calc_lat)) ** 2) + (cos(radians(lat1)) * cos(radians(lat2))) * (sin(radians(calc_long)) ** 2)
    d = calc_raio * asin(sqrt(parenteses))
    return d

###

def esta_na_lista(nome_pais, paises):

    for pais in paises:

        try:

            if pais[0] == nome_pais:

                return True

        except:

            return False

    return False

###

def normaliza(continentes):
    normalizado = {}
    for continente in continentes:
        for pais in continentes[continente]:
            normalizado[pais] = continentes[continente][pais]
            normalizado[pais]["continente"] = continente
    return normalizado

###

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
        letra = choice(pais_soletrado)

        if letra.lower() not in letras_restritas and letra not in caracteres_especiais:

            return letra

###

def sorteia_pais(paises):
    sorteado = choice(list(paises))
    return sorteado
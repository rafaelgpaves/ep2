from math import *
from random import *
from prettytable import PrettyTable
from termcolor import colored

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

###

def tabela_dicas(tentativas, dict_true):
    banco_de_dicas = {1: ["Cor da Bandeira", 4], 2: ["Letra da capital", 3], 3: ["Área", 6], 4: ["População", 5], 5: ["Continente", 7], 0: ["Sem dica", 0]}
    x = PrettyTable()
    x.field_names = ["Índice", "Tipo", "Custo"]
    for tipo_de_dica in banco_de_dicas:
        if banco_de_dicas[tipo_de_dica][1] < tentativas and dict_true[banco_de_dicas[tipo_de_dica][0]] == True:
            x.add_row([tipo_de_dica, banco_de_dicas[tipo_de_dica][0], str(banco_de_dicas[tipo_de_dica][1]) + " tentativas"])
    print(colored("\nMERCADO DE DICAS", "white", attrs=["bold"]))
    print(x)

def imprime_dicas(cores_ja_informadas, letras_ja_informadas, status_dicas, paises, pais_sorteado, continente_certo, dict_porcentagens):
    
    if len(cores_ja_informadas) != 0:
        texto = []
        for cor in cores_ja_informadas:
            texto.append(cor + " ({}%)".format(dict_porcentagens[cor]))
        print(" - Cores da bandeira: " + ", ".join(texto))

    if len(letras_ja_informadas) != 0:
        print(" - Letras da capital: " + ", ".join(letras_ja_informadas))

    if status_dicas["Área"] == False:
        print(" - Área: {} km2".format(paises[pais_sorteado]["area"]))

    if status_dicas["População"] == False:
        print(" - População: {} habitantes".format(paises[pais_sorteado]["populacao"]))

    if status_dicas["Continente"] == False:
        print(" - Continente: " + continente_certo)
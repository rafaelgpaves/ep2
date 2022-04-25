"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json

with open("dados.json", "r") as arquivo:
    dados = arquivo.read()
continentes = json.loads(dados)

"""condicoes iniciais do jogo:"""
tentativas = 20 #variavel que guarda o numero de tentativas restantes do jogador

paises = normaliza(continentes)
pais_sorteado = sorteia_pais(paises)
print(pais_sorteado)

raio_terra = 6371
lat1 = paises[pais_sorteado]["geo"]["latitude"] #latitude do pais sorteado
long1 = paises[pais_sorteado]["geo"]["longitude"] #longitude do pais sorteado

paises_e_distancias = []

print("Um país foi escolhido, tente adivinhar!")

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))

    entrada = input("Qual o seu palpite? ")

    if entrada == "desisto":

        print("O país era {}".format(pais_sorteado))

        jogo = False

    else:

        if entrada in paises and esta_na_lista(entrada, paises_e_distancias) == False:

            tentativas -= 1

            lat2 = paises[entrada]["geo"]["latitude"] #latitude do pais que o usuario digitou
            long2 = paises[entrada]["geo"]["longitude"] #longitude do pais que o usuario digitou
            d = haversine(raio_terra, lat1, long1, lat2, long2)

            if d <= 1000:
                cor = 32
            elif d < 2500:
                cor = 33
            elif d <= 5000:
                cor = 31
            elif d <= 10000:
                cor = 35
            else:
                cor = 34

            adiciona_em_ordem(entrada, d, paises_e_distancias)

            for pais in paises_e_distancias:
                print(('\033[0;{};40m {} \033[0;0m').format(cor, "{} --> {}".format(d, pais)))
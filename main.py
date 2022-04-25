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

print("Um país foi escolhido, tente adivinhar!")

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))

    entrada = input("Qual o seu palpite? ")

    if entrada == "desisto":

        jogo = False

    else:

        if entrada in paises and esta_na_lista(entrada, ) == False:

            tentativas -= 1

            lat2 = paises[entrada]["geo"]["latitude"] #latitude do pais que o usuario digitou
            long2 = paises[entrada]["geo"]["longitude"] #longitude do pais que o usuario digitou
            d = haversine(raio_terra, lat1, long1, lat2, long2)
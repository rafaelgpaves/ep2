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

print("Um país foi escolhido, tente adivinhar!")

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))

    entrada = input("Qual o seu palpite? ")

    if entrada == "desisto":

        jogo = False
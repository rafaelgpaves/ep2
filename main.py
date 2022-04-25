"""importando funcoes:"""
from funcoes import *

"""condicoes iniciais do jogo:"""
tentativas = 20 #variavel que guarda o numero de tentativas restantes do jogador
pais_sorteado = sorteia_pais()

print("Um país foi escolhido, tente adivinhar!")

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))

    entrada = input("Qual o seu palpite? ")

    if entrada == "desisto":

        jogo = False
"""importando funcoes e os dados dos paises:"""
from funcoes import *
from tabulate import tabulate
import json

with open("dados.json", "r") as arquivo:
    dados = arquivo.read()
continentes = json.loads(dados)

"""condicoes iniciais do jogo:"""
tentativas = 20 # variavel que guarda o numero de tentativas restantes do jogador
raio_terra = 6371

paises = normaliza(continentes)
pais_sorteado = sorteia_pais(paises)

print("Um país foi escolhido, tente adivinhar!")

"""criando banco de dicas"""

dicas = [["1", "Cor da Bandeira", "4 tentativas"], ["2", "Letra da capital", "3 tentativas"], ["3", "Área", "6 tentativas"],["4", "População", "5 tentativas"],["5", "Continente", "7 tentativas"], ["0", "Sem dica", "0 tentativas"]] 
tabela_dicas = tabulate(dicas, headers=["Índice", "Dica", "Custo"])

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))
    entrada = input("Qual o seu palpite?\nComandos: 'dica', 'desisto'\n>>> ")
    if entrada == "desisto":
        jogo = False
    elif entrada == "dica":
        print(tabela_dicas)
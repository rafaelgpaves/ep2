"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json
from tabulate import tabulate

with open("dados.json", "r") as arquivo:
    dados = arquivo.read()
continentes = json.loads(dados)

"""condicoes iniciais do jogo:"""
tentativas = 20 #variavel que guarda o numero de tentativas restantes do jogador

paises = normaliza(continentes)
pais_sorteado = sorteia_pais(paises)

raio_terra = 6371
lat1 = paises[pais_sorteado]["geo"]["latitude"] #latitude do pais sorteado
long1 = paises[pais_sorteado]["geo"]["longitude"] #longitude do pais sorteado

print("Um país foi escolhido, tente adivinhá-lo!")

"""criando banco de dicas"""
dicas = [["1", "Cor da Bandeira", "4 tentativas"], ["2", "Letra da capital", "3 tentativas"], ["3", "Área", "6 tentativas"],["4", "População", "5 tentativas"],["5", "Continente", "7 tentativas"], ["0", "Sem dica", "0 tentativas"]] 
tabela_dicas = tabulate(dicas, headers=["Índice", "Dica", "Custo"])


"""o jogo:"""
jogo = True
while jogo:
    print("Você tem {} tentativas".format(tentativas))
    entrada = input("Qual o seu palpite? ")
    if entrada == "desisto":
        jogo = False
    elif entrada == "dica":
        print(tabela_dicas)
    else:
        if entrada in paises and esta_na_lista(entrada, ) == False:
            tentativas -= 1
            lat2 = paises[entrada]["geo"]["latitude"] #latitude do pais que o usuario digitou
            long2 = paises[entrada]["geo"]["longitude"] #longitude do pais que o usuario digitou
            d = haversine(raio_terra, lat1, long1, lat2, long2)
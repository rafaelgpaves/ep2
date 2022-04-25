"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json
from tabulate import tabulate
from termcolor import colored

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

paises_e_distancias = []

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

        print("O país era {}".format(pais_sorteado))

        jogo = False
    elif entrada == "dica":
        print(tabela_dicas)
        dica_escolhida = int(input("\nEscolha uma dica! (1/2/3/4/5/0)\n >>> "))
    else:

        if entrada in paises and esta_na_lista(entrada, paises_e_distancias) == False:

            tentativas -= 1
            lat2 = paises[entrada]["geo"]["latitude"] #latitude do pais que o usuario digitou
            long2 = paises[entrada]["geo"]["longitude"] #longitude do pais que o usuario digitou
            d = haversine(raio_terra, lat1, long1, lat2, long2)

            adiciona_em_ordem(entrada, d, paises_e_distancias)

            for pais in paises_e_distancias:

                if pais[1] <= 1000:
                    cor = "green"
                elif pais[1] < 2500:
                    cor = "yellow"
                elif pais[1] <= 5000:
                    cor = "red"
                elif pais[1] <= 10000:
                    cor = "magenta"
                else:
                    cor = "blue"
                print(colored("{} --> {}".format(pais[1], pais[0]), cor, attrs=["bold"]))
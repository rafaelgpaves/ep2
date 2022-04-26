"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json
from tabulate import tabulate
from termcolor import colored

with open("dados.json", "r") as arquivo:
    dados = arquivo.read()
continentes = json.loads(dados)

"""condicoes iniciais do jogo:"""

paises = normaliza(continentes)

raio_terra = 6371

print("\nUm país foi escolhido, tente adivinhá-lo!")

"""o jogo:"""
jogo = True
while jogo:

    """condicoes da rodada atual:"""
    tentativas = 20 #variavel que guarda o numero de tentativas restantes do jogador
    pais_sorteado = sorteia_pais(paises)
    lat1 = paises[pais_sorteado]["geo"]["latitude"] #latitude do pais sorteado
    long1 = paises[pais_sorteado]["geo"]["longitude"] #longitude do pais sorteado
    paises_e_distancias = [] #lista que guarda os paises ja tentados pelo jogador
    cores_ja_informadas = []

    rodada = True
    while rodada:
        print("Você tem {} tentativas".format(tentativas))
        entrada = input("Qual o seu palpite? (comandos: 'dica' ou 'desisto')\n>>> ").lower()
        if entrada == "desisto":

            print("O país era {}".format(pais_sorteado))

            rodada = False

        elif entrada == "dica":
            dicas(tentativas)
            while True:
                dica_escolhida = int(input("\nEscolha uma dica! [1/2/3/4/5/0]\n>>> "))
                if dica_escolhida not in (1, 2, 3, 4, 5, 0):
                    continue
                else:
                    if dica_escolhida == 1:
                        cores_bandeira = []
                        for cor in paises[pais_sorteado]["bandeira"]:
                            if paises[pais_sorteado]["bandeira"][cor] != 0:
                                cores_bandeira.append(cor)
                            cor_sorteada = choice(cores_bandeira)
                            cores_ja_informadas.append(cor_sorteada)
                        print("\n A bandeira do país sorteado possui a cor {}.".format(cor_sorteada))


        else:

            if entrada in paises and esta_na_lista(entrada, paises_e_distancias) == False:

                tentativas -= 1
                lat2 = paises[entrada]["geo"]["latitude"] #latitude do pais que o usuario digitou
                long2 = paises[entrada]["geo"]["longitude"] #longitude do pais que o usuario digitou
                d = haversine(raio_terra, lat1, long1, lat2, long2)

                if d == 0:
                    print("Você acertou, parabéns!")
                    rodada = False

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
                    print(colored("{} km --> {}".format(int(pais[1]), pais[0]), cor, attrs=["bold"]))

    entrada_valida = True
    while entrada_valida:
        de_novo = input("Quer jogar de novo? [s/n] ").lower() 
        if de_novo.lower() == "s":
            entrada_valida = False
        elif de_novo.lower() == "n":
            print("\nObrigado por jogar!")
            entrada_valida = False
            jogo = False
        else:
            print("Digite apenas 's' ou 'n'")
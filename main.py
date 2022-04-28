"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json
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
    tentativas = 20 # variável que guarda o número de tentativas restantes do jogador
    pais_sorteado = sorteia_pais(paises) # país sorteado pelo jogo
    lat1 = paises[pais_sorteado]["geo"]["latitude"] # latitude do país sorteado
    long1 = paises[pais_sorteado]["geo"]["longitude"] # longitude do país sorteado
    paises_e_distancias = [] # lista que guarda os países já tentados pelo jogador
    cores_ja_informadas = [] # cores já informadas ao jogador pelo tipo de dica 1
    dicas_solicitadas = [] # dicas (gerais) já informadas ao jogador pelo sistema

    # criando uma lista com as cores da bandeira do país sorteado
    cores_bandeira = []
    for cor in paises[pais_sorteado]["bandeira"]:
        if paises[pais_sorteado]["bandeira"][cor] != 0:
            cores_bandeira.append(cor)

    rodada = True
    while rodada:

        if tentativas > 10:
            codigo_da_cor = 34
        elif tentativas > 5:
            codigo_da_cor = 33
        else:
            codigo_da_cor = 31
        print("Você tem {} tentativas".format('\033[1;{0};40m{1}\033[0;0m'.format(codigo_da_cor, tentativas)))

        if tentativas == 0:

            print("Acabaram as tentativas, que pena!")
            print("O país era {}".format(pais_sorteado))
            rodada = False
            continue

        entrada = input("Qual o seu palpite? (comandos: 'dica' ou 'desisto')\n>>> ").lower()
        if entrada == "desisto":

            print("O país era {}".format(pais_sorteado))

            rodada = False

        elif entrada == "dica":
            dicas(tentativas)
            while True:
                dica_escolhida = input("\nEscolha uma dica! [1/2/3/4/5/0]\n>>> ")
                if dica_escolhida not in ("1", "2", "3", "4", "5", "0"):
                    print("\nDesculpe, mas esse input é inválido\n")
                    continue
                else:
                    if dica_escolhida == "1":
                        if tentativas <= 4:
                            print("Desculpa, mas você nâo tem tentativas suficientes\n")
                            break
                        else:
                            if len(cores_bandeira) == len(cores_ja_informadas):
                                print("\nTodas as cores já foram informadas!\n")
                                break
                            else:
                                tentativas -= 4
                                
                                cor_invalida = True
                                while cor_invalida:
                                    cor_sorteada = choice(cores_bandeira)
                                    if cor_sorteada not in cores_ja_informadas:
                                        break

                                cores_ja_informadas.append(cor_sorteada)
                                dica_bandeira = "\nA bandeira do país sorteado possui a cor {}\n".format(cor_sorteada)
                                dicas_solicitadas.append(dica_bandeira)
                                print(dica_bandeira)
                                break


        else:

            if entrada in paises and esta_na_lista(entrada, paises_e_distancias) == False:

                tentativas -= 1
                lat2 = paises[entrada]["geo"]["latitude"] # latitude do país que o usuário digitou
                long2 = paises[entrada]["geo"]["longitude"] # longitude do país que o usuário digitou
                d = haversine(raio_terra, lat1, long1, lat2, long2)

                if d == 0:
                    print("Você acertou, parabéns!")
                    rodada = False

                adiciona_em_ordem(entrada, d, paises_e_distancias)

                print("Distâncias: ")
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

                # imprimindo as dicas
                print("\nDicas: ")
                if len(cores_ja_informadas) != 0:
                    print(" - Cores da bandeira: " + ", ".join(cores_ja_informadas))
                    # será que é mais facil fazer uma função para imprimir dicas?
                    # eu pensei em colocar em uma lista e pedir pra ele imprimir cada item da lista, mas pode ficar bagunçado

            elif entrada in paises and esta_na_lista(entrada, paises_e_distancias) == True:

                print("Você já digitou esse país")

            else:

                print("Esse país não consta no banco de dados")

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
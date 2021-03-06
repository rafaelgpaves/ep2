"""importando funcoes e os dados dos paises:"""
from funcoes import *
import json
import emoji

with open("dados.json", "r") as arquivo:
    dados = arquivo.read()
continentes = json.loads(dados)

"""condicoes iniciais do jogo:"""

paises = normaliza(continentes)

raio_terra = 6371

# printando o "título"
print("\n")
print(" " + ("=" * 18) + " ")
print("|" + (" " * 18) + "|")
print("|" + (" " * 1) + colored("Aᴅɪᴠɪɴʜᴇ ᴏ ᴘᴀís!", "cyan", attrs=["bold"]) + (" " * 1) +"|")
print("|" + (" " * 18) + "|")
print(" " + ("=" * 18) + " ")
print("por Bruno Zalcberg e Rafael Gordon Paves")

# printando os comandos:
print("\n")
print("Comandos: ")
print("    dica/dicas -- entra no mercado de dicas")
print("    desisto    -- desiste da rodada")
print("    inventario -- exibe suas dicas e distâncias")

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
    status_dicas = {"Cor da Bandeira": True, "Letra da capital": True, "Área": True, "População": True, "Continente": True, "Sem dica": True}
    cores_ja_informadas = [] # cores já informadas ao jogador pelo tipo de dica 1
    porcentagens = {} # dict que usamos para informar a porcentagem das cores na bandeira
    letras_ja_informadas = [] # letras já informadas ao jogador pelo tipo de dica 2
    letras_capital = 0 # total de letras na capital
    for letra in paises[pais_sorteado]["capital"]:
        letras_capital += 1
    area_com_ponto = "" #string que guarda a populacao do pais atual usando pontos a cada tres numeros (dica 3)
    populacao_com_ponto = "" #string que guarda a populacao do pais atual usando pontos a cada tres numeros (dica 4)
    dicas_solicitadas = [] # dicas (gerais) já informadas ao jogador pelo sistema

    # criando uma lista com as cores da bandeira do país sorteado
    cores_bandeira = []
    for cor in paises[pais_sorteado]["bandeira"]:
        if paises[pais_sorteado]["bandeira"][cor] != 0:
            cores_bandeira.append(cor)

    # removendo a cor "outros"
    if "outras" in cores_bandeira:
        cores_bandeira.remove("outras")

    # formatando a grafia do continente
    continente = paises[pais_sorteado]["continente"]
    if continente == "africa":
        continente_certo = "África"
    elif continente == "oceania":
        continente_certo = "Oceania"
    elif continente == "europa":
        continente_certo = "Europa"
    elif continente == "asia":
        continente_certo = "Ásia"
    elif continente == "america do norte":
        continente_certo = "América do Norte"
    elif continente == "america do sul":
        continente_certo = "América do Sul"

    rodada = True
    while rodada:

        if tentativas <= 0:

            print("\nAcabaram as tentativas, que pena!")
            print("O país era {}".format(pais_sorteado.title()))
            rodada = False
            continue
        
        if tentativas > 10:
            codigo_da_cor = 34
        elif tentativas > 5:
            codigo_da_cor = 33
        else:
            codigo_da_cor = 31
        print("\nVocê tem {} tentativas".format('\033[1;{0};40m{1}\033[0;0m'.format(codigo_da_cor, tentativas)))

        entrada = input("Qual o seu palpite?\n>>> ").lower()
        if entrada == "desisto":

            print("\nO país era {}".format(pais_sorteado.title()))

            rodada = False

        elif entrada == "dica" or entrada == "dicas":

            tabela_dicas(tentativas, status_dicas)
            while True:
                dica_escolhida = input("\nEscolha uma dica! " + opcoes(tentativas, status_dicas) + "\n>>> ")
                if dica_escolhida not in ("1", "2", "3", "4", "5", "0"):
                    print("\nDesculpe, mas esse input é inválido\n")
                    continue
                else:
                    if dica_escolhida == "1": # cor da bandeira
                        if tentativas > 4:
                            if status_dicas["Cor da Bandeira"] == False:
                                print("Desculpa, mas todas as cores já foram informadas.\n")
                            else:
                                tentativas -= 4
                                cor_invalida = True
                                while cor_invalida:
                                    cor_sorteada = choice(cores_bandeira)
                                    if cor_sorteada not in cores_ja_informadas:
                                        break
                                cores_ja_informadas.append(cor_sorteada)
                                if len(cores_bandeira) == len(cores_ja_informadas):
                                    status_dicas["Cor da Bandeira"] = False
                                porcentagens[cor_sorteada] = paises[pais_sorteado]["bandeira"][cor_sorteada]
                                dica_bandeira = "\n{0}% da bandeira do país é composta pela cor {1}".format(porcentagens[cor_sorteada], cor_sorteada)
                                dicas_solicitadas.append(dica_bandeira)
                                print(dica_bandeira)
                        else:
                            print("\nDesculpa, mas você não tem tentativas suficientes.")
                        break

                    if dica_escolhida == "2": # letra da capital
                        if tentativas > 3:
                            if status_dicas["Letra da capital"] == False:
                                print("Desculpa, mas você já recebeu todas as letras da capital.")
                            else:
                                tentativas -= 3
                                letra = sorteia_letra(paises[pais_sorteado]["capital"], letras_ja_informadas)
                                letras_ja_informadas.append(letra)
                                print("\nA capital do país contém a letra '{}'.".format(letra))
                                if len(letras_ja_informadas) >= letras_capital:
                                    status_dicas["Letra da capital"] = False
                        else:
                            print("\nDesculpa, mas você não tem tentativas suficientes.")
                        break

                    if dica_escolhida == "3": # área
                        if tentativas > 6:
                            if status_dicas["Área"] == False:
                                print("\nDesculpa, mas você já perguntou a área do país!")
                            else:
                                tentativas -= 6
                                area = str(paises[pais_sorteado]["area"])
                                contador = 0
                                for numero in range(len(area) -1, -1, -1):
                                    if contador == 3:
                                        area_com_ponto = "." + area_com_ponto
                                        contador = 0
                                    area_com_ponto = area[numero] + area_com_ponto
                                    contador += 1
                                print("\nA área do país sorteado é de {0} km2.".format(area_com_ponto))
                                status_dicas["Área"] = False
                        else:
                            print("\nDesculpa, mas você não tem tentativas suficientes.")
                        break

                    if dica_escolhida == "4": # população
                        if tentativas > 5:
                            if status_dicas["População"] == False:
                                print("\nDesculpa, mas você já perguntou a população do país!")
                            else:
                                tentativas -= 5
                                populacao = str(paises[pais_sorteado]["populacao"])
                                contador = 0
                                for numero in range(len(populacao) -1, -1, -1):
                                    if contador == 3:
                                        populacao_com_ponto = "." + populacao_com_ponto
                                        contador = 0
                                    populacao_com_ponto = populacao[numero] + populacao_com_ponto
                                    contador += 1
                                print("\nA população do país sorteado é de {0} habitantes.".format(populacao_com_ponto))
                                status_dicas["População"] = False
                        else:
                            print("\nDesculpa, mas você não tem tentativas suficientes.")
                        break

                    if dica_escolhida == "5": # continente
                        if tentativas > 7:
                            if status_dicas["Continente"] == False:
                                print("\nDesculpa, mas você já perguntou em que continente o país se encontra!")
                            else:
                                tentativas -= 7
                                print("\nO país sorteado se encontra na {0}.".format(continente_certo))
                                status_dicas["Continente"] = False
                        else:
                            print("\nDesculpa, mas você não tem tentativas suficientes.")
                        break
                    
                    if dica_escolhida == "0": # sem dica
                        print("\nOk, você não quer nenhuma dica!")
                        break
        
        elif entrada == "inventario":

            print("\nDistâncias: ")
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

                distancia_str = str(round(pais[1])) # string que guarda a distância do pais atual
                distancia_com_ponto = "" # string que guarda a distância do país atual usando pontos a cada três números
                contador = 0 # variável que conta o número de caracteres (quando é igual a 3, é adicionado um ponto)
                for numero in range(len(distancia_str) -1, -1, -1):
                    if contador == 3:
                        distancia_com_ponto = "." + distancia_com_ponto
                        contador = 0
                    distancia_com_ponto = distancia_str[numero] + distancia_com_ponto
                    contador += 1
                
                print(colored("{} km --> {}".format(distancia_com_ponto, pais[0]), cor, attrs=["bold"]))

            print("\nDicas: ")
            imprime_dicas(cores_ja_informadas, letras_ja_informadas, status_dicas, continente_certo, porcentagens, area_com_ponto, populacao_com_ponto)
        
        else:

            if entrada in paises and esta_na_lista(entrada, paises_e_distancias) == False:

                tentativas -= 1
                lat2 = paises[entrada]["geo"]["latitude"] # latitude do país que o usuário digitou
                long2 = paises[entrada]["geo"]["longitude"] # longitude do país que o usuário digitou
                d = haversine(raio_terra, lat1, long1, lat2, long2)

                if d == 0:
                    print("\nVocê acertou, parabéns!")
                    rodada = False

                adiciona_em_ordem(entrada, d, paises_e_distancias)

                print("\nDistâncias: ")
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

                    distancia_str = str(round(pais[1])) #string que guarda a distancia do pais atual
                    distancia_com_ponto = "" #string que guarda a distancia do pais atual usando pontos a cada tres numeros
                    contador = 0 #variavel que conta o numero de caracteres (quando eh igual a 3, eh adicionado um ponto)
                    for numero in range(len(distancia_str) -1, -1, -1):
                        if contador == 3:
                            distancia_com_ponto = "." + distancia_com_ponto
                            contador = 0
                        distancia_com_ponto = distancia_str[numero] + distancia_com_ponto
                        contador += 1

                    print(colored("{} km --> {}".format(distancia_com_ponto, pais[0]), cor, attrs=["bold"]))

                # imprimindo as dicas
                print("\nDicas: ")
                imprime_dicas(cores_ja_informadas, letras_ja_informadas, status_dicas, continente_certo, porcentagens, area_com_ponto, populacao_com_ponto)

            elif entrada in paises and esta_na_lista(entrada, paises_e_distancias) == True:

                print("\nVocê já digitou esse país")

            else:

                print("\nEsse país não consta no banco de dados")

    entrada_valida = True
    while entrada_valida:
        de_novo = input("\nQuer jogar de novo? [s|n]\n>>> ").lower() 
        if de_novo == "s":
            entrada_valida = False
        elif de_novo == "n":
            print("\nObrigado por jogar! " + emoji.emojize(":grinning_face_with_smiling_eyes:\n"))
            
            entrada_valida = False
            jogo = False
        else:
            print("\nDigite apenas 's' ou 'n'")
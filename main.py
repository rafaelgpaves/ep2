"""condicoes iniciais do jogo:"""
tentativas = 20 #variavel que guarda o numero de tentativas restantes do jogador


print("Um país foi escolhido, tente adivinhar!")

"""o jogo:"""
jogo = True
while jogo:

    print("Você tem {} tentativas".format(tentativas))
    entrada = input("Qual o seu palpite? ")
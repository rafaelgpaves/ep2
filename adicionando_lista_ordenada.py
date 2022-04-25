def adiciona_em_ordem(nome_pais, d, paises):

    if nome_pais in paises:

        return paises

    distancias = [d] #lista de distancias

    for pais in paises:

        distancias.append(pais[1])

    distancias.sort() #arruamndo as distancias em ordem crescente
    i = distancias.index(d) #indice da distancia desse pais
    paises.insert(i, [nome_pais, d])

    return paises
## {continente: {país: {info: "num"}}}

def normaliza(continentes):
    normalizado = {}
    for continente in continentes:
        for pais in continentes[continente]:
            normalizado[pais] = continentes[continente][pais]
            normalizado[pais]["continente"] = continente
    return normalizado
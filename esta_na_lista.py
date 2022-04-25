def esta_na_lista(nome_pais, paises):

    for pais in paises:

        try:

            if pais[0] == nome_pais:

                return True

        except:

            return False

    return False
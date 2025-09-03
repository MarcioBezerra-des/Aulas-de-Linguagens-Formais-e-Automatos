def e_palindromo(cadeia):
    cadeia_invertida = cadeia[::-1]

    if cadeia == cadeia_invertida:
        print(f"A cadeia '{cadeia}' é um palíndromo.")
        return True
    else:
        print(f"A cadeia '{cadeia}' não é um palíndromo.")
        return False

e_palindromo("arara")
e_palindromo("ovo")
e_palindromo("automato")
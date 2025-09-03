def simulador_automato_pilha_palindromo(cadeia):

    pilha = []
    marcador_encontrado = False
    print(f"Analisando: '{cadeia}'")

    for simbolo in cadeia:
        if simbolo == '#':
            if marcador_encontrado:
                print("Rejeitado: Múltiplos marcadores.")
                return False
            marcador_encontrado = True
            print("Marcador '#' encontrado. Iniciando fase de desempilhamento.")
            continue

        if not marcador_encontrado:
            pilha.append(simbolo)
            print(f"Empilhou '{simbolo}'. Pilha: {pilha}")
        else:
            if not pilha:
                print("Rejeitado: Cadeia mais longa após o marcador.")
                return False
            topo_pilha = pilha.pop()
            print(f"Leu '{simbolo}', desempilhou '{topo_pilha}'.")
            if simbolo != topo_pilha:
                print("Rejeitado: Símbolos não correspondem.")
                return False

    if not pilha and marcador_encontrado:
        print("Aceito: A cadeia foi lida e a pilha está vazia.")
        return True
    else:
        print("Rejeitado: A cadeia terminou, mas a pilha não está vazia ou o marcador não foi encontrado.")
        return False

simulador_automato_pilha_palindromo("ab#ba")
print("-" * 20)
simulador_automato_pilha_palindromo("abc#bca")
def verificador_parenteses_com_pilha(expressao):

    pilha = []
    mapeamento = {')': '(', ']': '[', '}': '{'}

    print(f"Verificando a expressão: {expressao}")

    for char in expressao:
        if char in mapeamento.values():
            pilha.append(char)
            print(f"Abriu '{char}', empilhou. Pilha: {pilha}")
        elif char in mapeamento.keys():
            if not pilha or pilha[-1] != mapeamento[char]:
                print(f"Erro: Fechou '{char}' inesperadamente. REJEITADO.")
                return False
            pilha.pop()
            print(f"Fechou '{char}', desempilhou. Pilha: {pilha}")

    if not pilha:
        print("Expressão balanceada corretamente. ACEITO.")
        return True
    else:
        print("Erro: Parênteses de abertura não foram fechados. REJEITADO.")
        return False

verificador_parenteses_com_pilha("({[]})")
print("-" * 20)
verificador_parenteses_com_pilha("([)]")
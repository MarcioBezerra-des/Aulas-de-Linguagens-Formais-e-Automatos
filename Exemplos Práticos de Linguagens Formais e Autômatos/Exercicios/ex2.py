def simulador_afd_termina_em_1(cadeia):
    
    estado_atual = 'q0'
    estados_finais = {'q1'}

    print(f"Analisando a cadeia: '{cadeia}'")

    for simbolo in cadeia:
        if estado_atual == 'q0':
            if simbolo == '0':
                estado_atual = 'q0'
            elif simbolo == '1':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == '0':
                estado_atual = 'q0'
            elif simbolo == '1':
                estado_atual = 'q1'
        print(f"Leu '{simbolo}', transição para -> {estado_atual}")

    if estado_atual in estados_finais:
        print(f"Resultado: A cadeia '{cadeia}' foi ACEITA.\n")
        return True
    else:
        print(f"Resultado: A cadeia '{cadeia}' foi REJEITADA.\n")
        return False

simulador_afd_termina_em_1("10101")
simulador_afd_termina_em_1("10100")
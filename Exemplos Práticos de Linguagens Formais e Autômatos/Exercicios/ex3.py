def maquina_turing_incremento_binario(binario_str):
    
    print(f"Incrementando o número binário: {binario_str}")
    fita = list(binario_str)
    posicao_cabecote = len(fita) - 1 

    while posicao_cabecote >= 0:
        if fita[posicao_cabecote] == '1':
            fita[posicao_cabecote] = '0'
            posicao_cabecote -= 1 
        else: # Encontrou um '0'
            fita[posicao_cabecote] = '1'
            print(f"Resultado: {''.join(fita)}")
            return ''.join(fita)

    resultado = '1' + ''.join(fita)
    print(f"Resultado: {resultado}")
    return resultado


maquina_turing_incremento_binario("1011") 
maquina_turing_incremento_binario("1111") 
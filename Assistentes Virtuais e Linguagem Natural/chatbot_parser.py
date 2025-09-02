def chatbot_parser(entrada):

    # Definição dos terminais da gramática
    comandos_validos = ["ligue", "desligue", "abra"]
    objetos_validos = ["luz", "portão", "música"]

    # Normaliza e divide a entrada em palavras (tokens)
    palavras = entrada.lower().split()

    # A gramática espera uma estrutura "Comando Objeto" (2 palavras)
    if len(palavras) != 2:
        return "Erro: Comando não reconhecido. Use o formato: 'Comando Objeto'."

    comando, objeto = palavras[0], palavras[1]

    # Verifica se as palavras correspondem às regras da gramática
    if comando in comandos_validos and objeto in objetos_validos:
        # Saída simulada
        return f"Ação executada: {comando.capitalize()} o(a) {objeto}."
    else:
        return "Erro: Comando ou objeto inválido."

# Exemplos de Entrada
entrada1 = "ligue luz"
entrada2 = "abra o portão" # Exemplo inválido para este parser simples
entrada3 = "desligue música"
entrada4 = "toque som"

print(f"Entrada: \"{entrada1}\"")
print(f"Saída: {chatbot_parser(entrada1)}\n")

print(f"Entrada: \"{entrada2}\"")
print(f"Saída: {chatbot_parser(entrada2)}\n") # Não corresponde à gramática "Comando Objeto"

print(f"Entrada: \"{entrada3}\"")
print(f"Saída: {chatbot_parser(entrada3)}\n")

print(f"Entrada: \"{entrada4}\"")
print(f"Saída: {chatbot_parser(entrada4)}\n")
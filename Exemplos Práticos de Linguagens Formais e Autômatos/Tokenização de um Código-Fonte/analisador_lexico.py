import re

def analisador_lexico(codigo_fonte):

    regras_tokens = [
        ('PALAVRA_CHAVE', r'\b(int|float|if|else|while|return)\b'),
        ('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('NUMERO', r'\d+'),
        ('OPERADOR', r'(=|\+|-|\*|/)'),
        ('DELIMITADOR',     r';'),
        ('ESPACO',          r'\s+'),  # Para ignorar espaços
        ('DESCONHECIDO',    r'.')   # Para qualquer outro caractere
    ]

    regex = '|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in regras_tokens)

    tokens = []

    for correspondencia in re.finditer(regex, codigo_fonte):
        tipo_token = correspondencia.lastgroup
        valor_token = correspondencia.group(tipo_token)
        if tipo_token != 'ESPACO':
            tokens.append((valor_token, tipo_token))

    return tokens

entrada = "int x = 10;"
tokens_gerados = analisador_lexico(entrada)

print(f"Entrada: \"{entrada}\"\n")
print("Tokens Gerados:")
print("-" * 25)
print(f"{'Token':<15} | {'Tipo'}")
print("-" * 25)
for token, tipo in tokens_gerados:
        print(f"{token:<15} | {tipo}")
print("-" * 25)
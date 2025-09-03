import random

def gerar_cadeia_regular(max_len=10):
    """Gera uma cadeia a partir de uma gramática regular."""
    resultado = ""
    for _ in range(random.randint(0, max_len - 1)):
        resultado += "a"
    resultado += "b"
    return resultado

def gerar_cadeia_livre_contexto(n=3):
    """Gera uma cadeia a partir de uma gramática livre de contexto."""
    if n <= 0:
        return ""
    else:
        return "a" + gerar_cadeia_livre_contexto(n - 1) + "b"

print("Complexidade Sintática - Geração de Cadeias:")
print(f"1. A partir de Gramática Regular: '{gerar_cadeia_regular()}'")
print(f"2. A partir de Gramática Livre de Contexto (n=4): '{gerar_cadeia_livre_contexto(4)}'")
print("\nNote como a segunda gramática impõe uma estrutura simétrica (complexidade) maior.")
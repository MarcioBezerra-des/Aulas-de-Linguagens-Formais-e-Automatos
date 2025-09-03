import re

def reconhece_regular(cadeia):
    padrao = re.compile(r'^(ab)+$')
    return bool(padrao.match(cadeia))

def reconhece_livre_contexto(cadeia):
    if not cadeia or 'a' not in cadeia or 'b' not in cadeia: return False
    ponto_de_virada = cadeia.find('b')
    parte_a = cadeia[:ponto_de_virada]
    parte_b = cadeia[ponto_de_virada:]
    return all(c == 'a' for c in parte_a) and \
           all(c == 'b' for c in parte_b) and \
           len(parte_a) == len(parte_b)

def reconhece_sensivel_contexto(cadeia):

    if not cadeia: return False
    try:
        idx_b = cadeia.index('b')
        idx_c = cadeia.index('c')
    except ValueError:
        return False
    parte_a = cadeia[:idx_b]
    parte_b = cadeia[idx_b:idx_c]
    parte_c = cadeia[idx_c:]
    return all(c == 'a' for c in parte_a) and \
           all(c == 'b' for c in parte_b) and \
           all(c == 'c' for c in parte_c) and \
           len(parte_a) == len(parte_b) == len(parte_c)

print(f"Poder Computacional Crescente:")
print(f"Regular ('abab'): {reconhece_regular('abab')}")
print(f"Livre de Contexto ('aaabbb'): {reconhece_livre_contexto('aaabbb')}")
print(f"Sensível ao Contexto ('aabbcc'): {reconhece_sensivel_contexto('aabbcc')}")
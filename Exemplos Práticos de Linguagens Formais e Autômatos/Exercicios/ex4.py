def reconhece_an_bn(cadeia):
   
    if not cadeia: 
        print(f"Cadeia '' pertence à linguagem (n=0). ACEITA.")
        return True

    try:
        ponto_de_virada = cadeia.index('b')
    except ValueError:
        print(f"Cadeia '{cadeia}' não tem 'b's. REJEITADA.")
        return False

    parte_a = cadeia[:ponto_de_virada]
    parte_b = cadeia[ponto_de_virada:]

    if any(c != 'a' for c in parte_a) or any(c != 'b' for c in parte_b):
        print(f"Cadeia '{cadeia}' está mal formada. REJEITADA.")
        return False

    if len(parte_a) == len(parte_b):
        print(f"Cadeia '{cadeia}' pertence à linguagem (n={len(parte_a)}). ACEITA.")
        return True
    else:
        print(f"Cadeia '{cadeia}' não pertence (nº de 'a's != nº de 'b's). REJEITADA.")
        return False

reconhece_an_bn("aaabbb")
reconhece_an_bn("aabb")
reconhece_an_bn("aaabb")
reconhece_an_bn("")
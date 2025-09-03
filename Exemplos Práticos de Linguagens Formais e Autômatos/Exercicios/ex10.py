import time

def loop_infinito():
    while True:
        pass

def termina_rapido():

    return "Terminei!"

def problema_da_parada_exemplo(funcao_alvo):
   
    print(f"Analisando a função: {funcao_alvo.__name__}")
   
    if funcao_alvo.__name__ == "loop_infinito":
        print("Resultado: Esta função parece nunca parar. (Limite da computação)")
    elif funcao_alvo.__name__ == "termina_rapido":
        print("Resultado: Esta função claramente para.")

print("Estudando os Limites da Computação: O Problema da Parada")
problema_da_parada_exemplo(termina_rapido)
print("-" * 20)
problema_da_parada_exemplo(loop_infinito)
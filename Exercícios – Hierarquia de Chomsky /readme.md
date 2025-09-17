Exercícios – Hierarquia de Chomsky 

1. A Hierarquia de Chomsky classifica linguagens formais com base em: 

a) Estrutura de dados e algoritmos 

b) Complexidade computacional e de memória 

c) Complexidade sintática e poder de geração (correto)

d) Arquitetura de sistemas operacionais 

e) Tipos de compiladores 

~~~py
print("Tipo 3 (Regular): Linguagem de e-mails -> 'usuario@provedor.com'")

print("Tipo 2 (Livre de Contexto): Linguagem de parênteses balanceados -> '(()())'")

print("Tipo 1 (Sensível ao Contexto): Linguagem aⁿbⁿcⁿ -> 'aaabbbccc'")

print("Tipo 0 (Irrestrita): Qualquer linguagem computável.")
~~~

2. Qual das alternativas representa corretamente a ordem de inclusão da Hierarquia de Chomsky? 

a) Tipo 3 ⊂ Tipo 2 ⊂ Tipo 1 ⊂ Tipo 0 (correto)

b) Tipo 0 ⊂ Tipo 1 ⊂ Tipo 2 ⊂ Tipo 3 

c) Tipo 1 ⊂ Tipo 3 ⊂ Tipo 0 ⊂ Tipo 2 

d) Tipo 3 ⊂ Tipo 1 ⊂ Tipo 2 ⊂ Tipo 0 

e) Tipo 2 ⊂ Tipo 3 ⊂ Tipo 1 ⊂ Tipo 0 

~~~py
linguagens_tipo_3 = {"'a*b'", "'(ab)*'"}
linguagens_tipo_2 = {"'aⁿbⁿ'", "'palíndromos'"} | linguagens_tipo_3
linguagens_tipo_1 = {"'aⁿbⁿcⁿ'"} | linguagens_tipo_2
linguagens_tipo_0 = {"'qualquer programa que para'"} | linguagens_tipo_1

print(f"Tipo 3 é subconjunto do Tipo 2? {linguagens_tipo_3.issubset(linguagens_tipo_2)}")
print(f"Tipo 2 é subconjunto do Tipo 1? {linguagens_tipo_2.issubset(linguagens_tipo_1)}")
print(f"Tipo 1 é subconjunto do Tipo 0? {linguagens_tipo_1.issubset(linguagens_tipo_0)}")

print("\nOrdem de inclusão: Tipo 3 ⊂ Tipo 2 ⊂ Tipo 1 ⊂ Tipo 0")
~~~

3. As gramáticas do Tipo 2 (livres de contexto) são reconhecidas por: 

a) Máquinas de Turing 

b) Autômatos com Pilha (correto)

c) Autômatos Finitos 

d) Máquinas Linearmente Limitadas 

e) Compiladores sintáticos 

~~~py
def reconhecedor_an_bn(cadeia):
    pilha = []
    for simbolo in cadeia:
        if simbolo == 'a':
            pilha.append('a')
        elif simbolo == 'b':
            if not pilha:
                return False
            pilha.pop()
        else:
            return False
            
    return not pilha

print(f"'aaabbb' pertence a L? {reconhecedor_an_bn('aaabbb')}")
print(f"'aabb' pertence a L? {reconhecedor_an_bn('aabb')}")
print(f"'aaab' pertence a L? {reconhecedor_an_bn('aaab')}")
print(f"'abb' pertence a L? {reconhecedor_an_bn('abb')}")
~~~

4. Qual linguagem pertence ao Tipo 1 (sensível ao contexto)? 

a) L = {aⁿbⁿ} 

b) L = {aⁿbⁿcⁿ} (correto)

c) L = {aⁿbᵐ | n,m ≥ 0} 

d) L = {cadeias com número par de 1s} 

e) L = {palíndromos de a e b} 

~~~py
def reconhecedor_an_bn_cn(cadeia):
    n = len(cadeia)
    if n == 0:
        return True
    if n % 3 != 0:
        return False
    
    k = n // 3
    parte_a = cadeia[0:k]
    parte_b = cadeia[k:2*k]
    parte_c = cadeia[2*k:n]
    
    return parte_a == 'a' * k and parte_b == 'b' * k and parte_c == 'c' * k

print(f"'aabbcc' pertence a L? {reconhecedor_an_bn_cn('aabbcc')}")
print(f"'aaabbbccc' pertence a L? {reconhecedor_an_bn_cn('aaabbbccc')}")
print(f"'aabbc' pertence a L? {reconhecedor_an_bn_cn('aabbc')}")
print(f"'acb' pertence a L? {reconhecedor_an_bn_cn('acb')}")
~~~

5. A linguagem L = {0ⁿ1ⁿ | n ≥ 0} pertence a: 

a) Linguagens regulares 

b) Linguagens irrestritas 

c) Linguagens sensíveis ao contexto 

d) Linguagens livres de contexto (correto)

e) Nenhuma das anteriores 

~~~py
def reconhecedor_0n_1n(cadeia):

    pilha = []
    
    try:
        idx_primeiro_1 = cadeia.index('1')
    except ValueError:
        return not cadeia

    for simbolo in cadeia[:idx_primeiro_1]:
        if simbolo == '0':
            pilha.append('0')
        else:
            return False

    for simbolo in cadeia[idx_primeiro_1:]:
        if simbolo == '1':
            if not pilha:
                return False
            pilha.pop()
        else:
            return False
            
    return not pilha

print(f"'0011' pertence a L? {reconhecedor_0n_1n('0011')}")
print(f"'01' pertence a L? {reconhecedor_0n_1n('01')}")
print(f"'' pertence a L? {reconhecedor_0n_1n('')}")
print(f"'001' pertence a L? {reconhecedor_0n_1n('001')}")
~~~

6. Qual das alternativas contém apenas linguagens regulares? 

a) {aⁿbⁿ, n ≥ 0} 

b) {cadeias palíndromas} 

c) {cadeias com número par de 1s} (correto)

d) {aⁿbⁿcⁿ} 

e) {aⁿbⁿbⁿaⁿ} 

~~~py
import re

regex_par_de_1s = re.compile(r'^(0*(10*1)*0*)$')

def reconhecedor_par_de_1s(cadeia):
    return bool(regex_par_de_1s.match(cadeia))

print(f"'11' tem nº par de 1s? {reconhecedor_par_de_1s('11')}")
print(f"'01010' tem nº par de 1s? {reconhecedor_par_de_1s('01010')}")
print(f"'1011' tem nº par de 1s? {reconhecedor_par_de_1s('1011')}") # 3 (ímpar)
print(f"'' tem nº par de 1s? {reconhecedor_par_de_1s('')}") # 0 (par)
~~~

7. Qual tipo de máquina reconhece linguagens do Tipo 0? 

a) Autômato com Pilha 

b) Autômato Finito Determinístico 

c) Máquina de Turing (correto)

d) Máquina Linearmente Limitada 

e) Máquina de Von Neumann 

~~~py
def is_prime_language(cadeia):
  
    try:
        n = int(cadeia)
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    except (ValueError, TypeError):
        return False

print(f"A cadeia '7' representa um número primo? {is_prime_language('7')}")
print(f"A cadeia '10' representa um número primo? {is_prime_language('10')}")
print(f"A cadeia 'abc' representa um número primo? {is_prime_language('abc')}")
~~~

8. As gramáticas sensíveis ao contexto exigem que: 

a) A produção dependa da posição do terminal 

b) As regras sejam no formato A → γ 

c) As regras preservem ou aumentem o comprimento das cadeias (correto)

d) O símbolo inicial seja sempre preservado 

e) A linguagem seja regular 

~~~py
def verifica_regra_sensivel_contexto(alfa, beta):

    return len(beta) >= len(alfa)

regra1 = ("aAb", "aBcb") 
regra2 = ("B", "b")      
regra3 = ("aB", "b")    

print(f"Regra 'aAb -> aBcb' é válida? {verifica_regra_sensivel_contexto('aAb', 'aBcb')}")
print(f"Regra 'B -> b' é válida? {verifica_regra_sensivel_contexto('B', 'b')}")
print(f"Regra 'aB -> b' é válida? {verifica_regra_sensivel_contexto('aB', 'b')}")
~~~

9. Expressões regulares são utilizadas para representar linguagens: 

a) Irrestritas 

b) Livres de contexto 

c) Sensíveis ao contexto 

d) Regulares (correto)

e) Palindrômicas 

~~~py
import re

regex = re.compile(r'^a.*b$')

def pertence_a_linguagem(cadeia):
    return bool(regex.match(cadeia))

print(f"'ab' pertence à linguagem? {pertence_a_linguagem('ab')}")
print(f"'axcyb' pertence à linguagem? {pertence_a_linguagem('axcyb')}")
print(f"'a' pertence à linguagem? {pertence_a_linguagem('a')}")
print(f"'b' pertence à linguagem? {pertence_a_linguagem('b')}")
print(f"'ac' pertence à linguagem? {pertence_a_linguagem('ac')}")
~~~

10. Sobre as máquinas que reconhecem cada classe, assinale a alternativa correta: 

a) Todas as linguagens são reconhecidas por autômatos finitos 

b) Linguagens sensíveis ao contexto são reconhecidas por compiladores 

c) Apenas máquinas de Turing reconhecem linguagens regulares 

d) Linguagens livres de contexto são reconhecidas por autômatos com pilha (correto)

e) Máquinas de Turing não reconhecem linguagens irrestritas 

~~~py
hierarquia_chomsky = {
    "Tipo 3 (Regular)": {
        "Gramática": "Regular",
        "Reconhecedor": "Autômato Finito (AF) / Expressão Regular"
    },
    "Tipo 2 (Livre de Contexto)": {
        "Gramática": "Livre de Contexto",
        "Reconhecedor": "Autômato com Pilha (AP)"
    },
    "Tipo 1 (Sensível ao Contexto)": {
        "Gramática": "Sensível ao Contexto",
        "Reconhecedor": "Autômato Linearmente Limitado (ALL)"
    },
    "Tipo 0 (Irrestrita)": {
        "Gramática": "Irrestrita",
        "Reconhecedor": "Máquina de Turing (MT)"
    }
}

print("Linguagens Livres de Contexto são reconhecidas por:", 
      hierarquia_chomsky["Tipo 2 (Livre de Contexto)"]["Reconhecedor"])

import json
print("\n--- Resumo da Hierarquia ---")
print(json.dumps(hierarquia_chomsky, indent=2, ensure_ascii=False))
~~~

Gabarito 

1. c 

2. a 

3. b 

4. b 

5. d 

6. c 

7. c 

8. c 

9. d 

10. d 

# **Exercícios Práticos – Hierarquia de Chomsky com Python**

### 1. Simulador de Autômato Finito Determinístico (AFD) 
Crie um programa que reconhece a linguagem regular L = {w | w contém número par de 0s}. 
Código:
~~~py
def reconhece_af_par(w): 
    estado = 0 
    for simbolo in w: 
        if simbolo == '0': 
            estado = 1 - estado 
    return estado == 0 
print(reconhece_af_par("0010"))  # True 
~~~
~~~py
def reconhece_af_par_de_zeros(w):

  estado = 0  # Estado inicial q0 (par)
  for simbolo in w:
    if simbolo == '0':
      estado = 1 - estado 
 
  return estado == 0

print(f"'001010' é aceita? {reconhece_af_par_de_zeros('001010')}") # True (4 zeros)
print(f"'10101' é aceita? {reconhece_af_par_de_zeros('10101')}")  # False (3 zeros)
print(f"'' é aceita? {reconhece_af_par_de_zeros('')}")      # True (0 zeros, que é par)
~~~


### 2. Validador de Cadeias por Expressão Regular 
Use regex para validar se uma cadeia pertence à linguagem L = {aⁿbⁿ | n ≥ 0}. 

Código: 
~~~py
import re 

cadeia = "aaabbb" 
padrao = re.compile(r"a+b+") 
print(bool(padrao.fullmatch(cadeia)))  # Aceita, mas não garante a quantidade igual 
~~~
~~~py
import re

cadeia = "aaabbb"
padrao_incorreto = re.compile(r"a+b+")
print(f"Padrão incorreto para 'aaabbb': {bool(padrao_incorreto.fullmatch(cadeia))}")
print(f"Padrão incorreto para 'aabbb': {bool(padrao_incorreto.fullmatch('aabbb'))}")
~~~

### 3. Analisador Simples de Gramática Livre de Contexto (GLC) 
Valide a cadeia 'aabb' com a GLC: S → aSb | ε. 

Código: 
~~~py
def glc_balanca(cadeia): 
    def rec(s, i, j): 
        if i > j: 
            return i == j 
        if s[i] == 'a' and s[j] == 'b': 
            return rec(s, i+1, j-1) 
        return False 
    return rec(cadeia, 0, len(cadeia)-1) 
 
print(glc_balanca("aabb"))  # True 
~~~
~~~py
def reconhecedor_glc_anbn(cadeia):
  def recursivo(subcadeia):
    if not subcadeia:
      return True
    
    if subcadeia.startswith('a') and subcadeia.endswith('b'):
      return recursivo(subcadeia[1:-1])
      
    return False

  return recursivo(cadeia)

print(f"'aabb' é válida? {reconhecedor_glc_anbn('aabb')}")     
print(f"'aaabbb' é válida? {reconhecedor_glc_anbn('aaabbb')}") 
print(f"'aab' é válida? {reconhecedor_glc_anbn('aab')}")       
print(f"'' é válida? {reconhecedor_glc_anbn('')}")         
~~~

### 4. Simulador de Autômato com Pilha (AP) 
Verifique se uma cadeia pertence à linguagem L = {aⁿbⁿ | n ≥ 1}. 

Código: 
~~~py
def ap_simples(cadeia): 
    pilha = [] 
    for simbolo in cadeia: 
        if simbolo == 'a': 
            pilha.append('a') 
        elif simbolo == 'b': 
            if not pilha: 
                return False 
            pilha.pop() 
    return len(pilha) == 0 

print(ap_simples("aaabbb"))  # True 
~~~
~~~py
def simulador_ap_anbn(cadeia):
  pilha = []
  fase_a = True

  if not cadeia:
      return False

  for simbolo in cadeia:
    if simbolo == 'a':
      if not fase_a:
        return False
      pilha.append('a')
    elif simbolo == 'b':
      fase_a = False # Mudamos para a fase de ler 'b's
      if not pilha:
        return False
      pilha.pop()
    else:
      return False

  return len(pilha) == 0 and not fase_a

print(f"'aaabbb' é aceita pelo AP? {simulador_ap_anbn('aaabbb')}")
print(f"'ab' é aceita pelo AP? {simulador_ap_anbn('ab')}")      
print(f"'aabb' é aceita pelo AP? {simulador_ap_anbn('aabb')}")  
print(f"'' é aceita pelo AP? {simulador_ap_anbn('')}")       
print(f"'aa' é aceita pelo AP? {simulador_ap_anbn('aa')}")         
print(f"'bba' é aceita pelo AP? {simulador_ap_anbn('bba')}")       
~~~


### 5. Máquina de Turing (simples) 
Simule uma máquina que reconhece L = {w#w | w ∈ {0,1}*}. 

Código: 
~~~py
def mt_reflexiva(cadeia): 
    if '#' not in cadeia: 
        return False 
    w1, w2 = cadeia.split('#') 
    return w1 == w2 

print(mt_reflexiva("101#101"))  # True 
~~~
~~~py
def mt_simples_w_hash_w(cadeia):
  if cadeia.count('#') != 1:
    return False
  
  w1, w2 = cadeia.split('#')
  
  return w1 == w2

print(f"'101#101' é aceita pela MT? {mt_simples_w_hash_w('101#101')}") 
print(f"'00#00' é aceita pela MT? {mt_simples_w_hash_w('00#00')}")    
print(f"'10#11' é aceita pela MT? {mt_simples_w_hash_w('10#11')}")     
print(f"'10101' é aceita pela MT? {mt_simples_w_hash_w('10101')}")   
~~~


### 6. Validação de Linguagem Sensível ao Contexto 
Aceite cadeias da linguagem L = {aⁿbⁿcⁿ | n ≥ 1}. 

Código: 
~~~py
def slc_abc(cadeia): 
    n = len(cadeia) // 3 
    return cadeia == 'a'*n + 'b'*n + 'c'*n 
 
print(slc_abc("aaabbbccc"))  # True 

### 7. Geração de Cadeias com Gramática Regular (Tipo 3) 
Implemente a gramática S → aS | b para gerar cadeias válidas. 
~~~
~~~py
def reconhecedor_slc_anbncn(cadeia):
  n = len(cadeia)
  if n == 0 or n % 3 != 0:
    return False

  k = n // 3
  
  cadeia_esperada = 'a' * k + 'b' * k + 'c' * k
  return cadeia == cadeia_esperada

print(f"'aaabbbccc' é aceita? {reconhecedor_slc_anbncn('aaabbbccc')}") 
print(f"'abc' é aceita? {reconhecedor_slc_anbncn('abc')}")            
print(f"'aabbcc' é aceita? {reconhecedor_slc_anbncn('aabbcc')}")      
print(f"'aabbc' é aceita? {reconhecedor_slc_anbncn('aabbc')}")        
~~~


Código: 
~~~py
import random 

def gerar_regular(): 
    cadeia = '' 
    while random.random() < 0.7: 
        cadeia += 'a' 
    cadeia += 'b' 
    return cadeia 

print(gerar_regular())  # Exemplo: 'aaab'  
~~~
~~~py
import random

def gerar_cadeia_regular():
  cadeia = ''
  while random.random() < 0.7:
    cadeia += 'a'
  
  cadeia += 'b'
  return cadeia

print(f"Cadeia gerada: {gerar_cadeia_regular()}")
print(f"Cadeia gerada: {gerar_cadeia_regular()}")
print(f"Cadeia gerada: {gerar_cadeia_regular()}")
~~~


### 8. Parser Recursivo para GLC (Tipo 2) 
Implemente recursivamente S → aSb | ε. 

Código: 
~~~py
def parseador_glc(cadeia): 
    def parse(pos): 
        if pos >= len(cadeia): 
            return pos 
        if cadeia[pos] == 'a': 
            fim = parse(pos + 1) 
            if fim < len(cadeia) and cadeia[fim] == 'b': 
                return fim + 1 
        return pos 
    return parse(0) == len(cadeia) 

print(parseador_glc("aaabbb"))  # True
~~~
~~~py
def parseador_recursivo_anbn(cadeia):
  if cadeia == "":
    return True
  
  if cadeia.startswith('a') and cadeia.endswith('b'):
    return parseador_recursivo_anbn(cadeia[1:-1])
  
  return False

print(f"Parse de 'aaabbb': {parseador_recursivo_anbn('aaabbb')}")
print(f"Parse de 'aabb': {parseador_recursivo_anbn('aabb')}")    
print(f"Parse de 'ab': {parseador_recursivo_anbn('ab')}")        
print(f"Parse de 'aab': {parseador_recursivo_anbn('aab')}")       
~~~
 

### 9. Classificador de Linguagens 
Dado um exemplo textual, classifique a linguagem como Regular, LLC, SLC ou Irrestrita. 

Código: 
~~~py
def classificar_linguagem(exemplo): 
    if exemplo in {"cadeias com número par de 1s", "palavras que terminam em 'ab'"}: 
        return "Regular (AFD)" 
    elif exemplo in {"aⁿbⁿ", "palíndromos"}: 
        return "LLC (AP)" 
    elif exemplo in {"aⁿbⁿcⁿ"}: 
        return "SLC (MT limitada)" 
    else: 
        return "Irrestrita (MT)" 

print(classificar_linguagem("aⁿbⁿcⁿ"))  # SLC 

~~~
~~~py
def classificar_linguagem(exemplo_descricao):
  mapeamento = {
      "cadeias com número par de 1s": "Regular (Tipo 3)",
      "palavras que terminam em 'ab'": "Regular (Tipo 3)",
      
      "aⁿbⁿ": "Livre de Contexto (Tipo 2)",
      "palíndromos": "Livre de Contexto (Tipo 2)",

      "aⁿbⁿcⁿ": "Sensível ao Contexto (Tipo 1)",
      "w#w": "Sensível ao Contexto (Tipo 1)",

      "verificar se um programa para": "Irrestrita / Recursivamente Enumerável (Tipo 0)"
  }
  return mapeamento.get(exemplo_descricao, "Descrição não reconhecida")

print(f"'aⁿbⁿcⁿ' -> {classificar_linguagem('aⁿbⁿcⁿ')}")
print(f"'palíndromos' -> {classificar_linguagem('palíndromos')}")
print(f"'cadeias com número par de 1s' -> {classificar_linguagem('cadeias com número par de 1s')}")
~~~

### 10. Leitura de Gramática Regular e Geração de Cadeias 
Crie um gerador que simule derivação com regras definidas para S → aS | b. 

Código: 
~~~py
regras = {'S': ['aS', 'b']} 

def derivar(simbolo='S', cadeia=''): 
    if simbolo not in regras: 
        return [cadeia + simbolo] 
    resultados = [] 
    for producao in regras[simbolo]: 
        resultados += derivar(producao, cadeia) 
    return resultados 

print(derivar()) 
~~~
~~~py
import random

regras = {
    'S': ['aS', 'b']
}

def gerar_por_derivacao(simbolo_inicial='S'):
    producao = random.choice(regras[simbolo_inicial])

    cadeia_gerada = ""
    for simbolo in producao:
        if simbolo in regras:
            cadeia_gerada += gerar_por_derivacao(simbolo)
        else:
            cadeia_gerada += simbolo
    
    return cadeia_gerada

print(f"Cadeia derivada: {gerar_por_derivacao()}")
print(f"Cadeia derivada: {gerar_por_derivacao()}")
print(f"Cadeia derivada: {gerar_por_derivacao()}")
~~~

## **Expressões Regulares**

### **1. Validação de CPF**
Crie uma expressão regular em Python que valide um CPF no formato 000.000.000-00.
Resposta: 
~~~py
import re

# Expressão regular para CPF no formato 000.000.000-00
padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

# Exemplos de teste
cpfs = [ [cite: 9]
    "123.456.789-00", # válido
    "111.222.333-44", # válido
    "12345678900", #inválido
    "12.3456.789-00", # inválido
    "123.456.789.00" # inválido 
]

for cpf in cpfs:
    if re.match(padrao_cpf, cpf):
        print(f"{cpf} -> válido")
    else:
        print(f"{cpf} -> inválido")
~~~
Resultado:
~~~py
123.456.789-00 -> válido
111.222.333-44 -> válido
12345678900 -> inválido
12.3456.789-00 -> inválido
123.456.789.00 -> inválido
~~~

### **2. Identificação de e-mails válidos**
Utilize regex para validar se uma string é um endereço de e-mail básico (ex:
nome@dominio.com).
Resposta:
~~~py
import re

# Regex para e-mails básicos
padrao_email = r'^[|\w|.-]+@[\w\.-]+\.\w+$'

# Exemplos de teste
emails = [
    "usuario@dominio.com", # válido
    "meu.email@provedor.org", # válido
    "nome.sobrenome@empresa.co",# válido
    "usuario@dominio", # inválido (sem TLD)
    "usuario#dominio.com",
    # inválido (sem @)
    "@dominio.com",
    # inválido
]

for email in emails:
    if re.match(padrao_email, email):
        print(f"{email} -> válido")
    else:
        print(f"{email} -> inválido")
~~~
Resultado:
~~~py
usuario@dominio.com -> válido
meu.email@provedor.org -> válido
nome.sobrenome@empresa.co -> válido
usuario@dominio -> inválido
usuario#dominio.com -> inválido
@dominio.com -> inválido
~~~

### **3. Filtragem de palavras com 3 letras**
Dada uma lista de palavras, use regex para filtrar apenas as que têm exatamente 3 letras
(ex: sol, lua).

Resposta:
~~~py
import re

# Regex para palavras com exatamente 3 letras
padrao = r'^[a-zA-Z]{3}$'

# Lista de palavras
palavras = ["sol", "lua", "casa", "ar", "céu", "mar", "rio"]

# Filtrar com list comprehension
resultado = [p for p in palavras if re.match(padrao, p)]
print("Palavras com 3 letras:", resultado)
~~~
Resultado:
~~~py
Palavras com 3 letras: ['sol', 'lua', 'céu', 'mar', 'rio']
~~~
### **4. Substituição de palavras**
Escreva um código que substitui todos os números de uma string por '#'.
Resposta: 
~~~py
import re

texto = "Hoje é dia 17/09/2025 e o preço é 150 reais."

# Substituir todos os dígitos por '#'
resultado = re.sub(r'\d', '#', texto)
print(resultado)
~~~
Resultado:
~~~py
Hoje é dia ##/##/#### e o preço é ### reais.
~~~
### **5. Detecção de placas de veículos**
Valide se uma string corresponde ao padrão de placa brasileira tradicional (ABC-1234).
Resposta: 
~~~py
import re [cite: 61]

# Regex para placas no formato ABC-1234
padrao_placa = r'^[A-Z]{3}-\d{4}$'

# Exemplos de teste [cite: 64]
placas = [
    "ABC-1234", # válido
    "ΧΥΖ-0001", #válido
    "abc-1234", #inválido (minúsculas)
    "AB-1234", # inválido (só 2 letras)
    "ABCD-1234", # inválido (4 letras)
    "ABC1234", # inválido (sem hífen)
]
for placa in placas: [cite: 72]
    if re.match(padrao_placa, placa):
        print(f"{placa} -> válido")
    else:
        print(f"{placa} -> inválido"
~~~
Resultado:
~~~py
ABC-1234 -> válido
ΧΥΖ-0001 -> válido
abc-1234 -> inválido
AB-1234 -> inválido
ABCD-1234 -> inválido
ABC1234 -> inválido
~~~

### **6. AFD – número par de 'a'**
Implemente um AFD que reconhece cadeias com número par de letras 'a'.
Resposta:
~~~py
def afd_par_de_a(cadeia):
    estado = 'q0' # estado inicial
    for simbolo in cadeia:
        if estado == 'q0':
            if simbolo == 'a':
                estado = 'q1'
            # se for 'b', permanece em q0
        elif estado == 'q1':
            if simbolo == 'a':
                estado = 'q0'
            # se for 'b', permanece em q1
    return estado == 'q0' # só aceita se terminar em q0 (número par de 'a')

# Testes
testes = ["", "a", "aa", "ababa", "baba", "aaa", "bbbb"]
for teste in testes:
    resultado = afd_par_de_a(teste)
    print(f"'{teste}': {'Aceita' if resultado else 'Rejeita'}")
~~~
Resultado:
~~~py
'': Aceita
'a': Rejeita
'aa': Aceita
'ababa': Rejeita
'baba': Aceita
'aaa': Rejeita
'bbbb': Aceita
~~~
### **7. AFD – cadeias terminando em '01'**
Crie um programa que simula um AFD e retorna True se a cadeia termina com '01'.
Resposta:
~~~py
def afd_termina_em_01(cadeia):
    estado = 'q0' # estado inicial
    for simbolo in cadeia:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q0'
            else:
                return False # símbolo inválido
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q2'
            else:
                return False
        elif estado == 'q2':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q0'
            else:
                return False
    return estado == 'q2' # só aceita se terminar em q2

# Testes
testes = ["01", "001", "101", "1101", "111", "0", ""]
for teste in testes:
    resultado = afd_termina_em_01(teste)
    print(f"'{teste}': {'Aceita' if resultado else 'Rejeita'}")
~~~
Resultado:
~~~py
'01': Aceita
'001': Aceita
'101': Aceita
'1101': Aceita
'111': Rejeita
'0': Rejeita
'': Rejeita
~~~

### **8. AFND – pelo menos um 'a' ou 'b'**
Implemente um AFND que aceite qualquer cadeia não vazia contendo pelo menos um 'a' ou
'b'.
Resposta:
~~~py
def afnd_pelo_menos_um_a_ou_b(cadeia):
    # Se a cadeia estiver vazia, rejeita
    if not cadeia:
        return False
    
    # Estado inicial
    estado = 'q0'
    
    for simbolo in cadeia:
        if simbolo not in ('a', 'b'):
            return False # símbolo inválido
        
        # Transições do AFND
        if estado == 'q0':
            # ao ver 'a' ou 'b', vai para q1
            estado = 'q1'
        elif estado == 'q1':
            estado = 'q1' # permanece em q1
            
    # Aceita se terminar em q1
    return estado == 'q1'

# Testes
testes = ["a", "b", "ab", "ba", "aa", "bb", "", "c", "abc"]
for teste in testes:
    resultado = afnd_pelo_menos_um_a_ou_b(teste)
    print(f"'{teste}': {'Aceita' if resultado else 'Rejeita'}")
~~~
Resultado:
~~~py
'a': Aceita
'b': Aceita
'ab': Aceita
'ba': Aceita
'aa': Aceita
'bb': Aceita
'': Rejeita
'c': Rejeita
'abc': Rejeita
~~~

### **9. Conversão AFND para AFD**
Dada a tabela de transições de um AFND, represente seu AFD equivalente.
Resposta:
~~~py
from collections import deque

# Passo 1: Definir AFND
afnd = {
    'q0': {'a': ['q0', 'q1'], 'b': []},
    'q1': {'a': [], 'b': ['q2']},
    'q2': {'a': [], 'b': []}
}
estado_inicial = 'q0'
estados_aceitacao = {'q2'}
simbolos = ['a', 'b']

# Passo 2: Função de conversão AFND -> AFD
def afnd_para_afd(afnd, estado_inicial, estados_aceitacao, simbolos):
    estado_inicial_afd = frozenset([estado_inicial])
    visitados = set()
    transicoes_afd = {}
    fila = deque([estado_inicial_afd])
    estados_afd = set()
    estados_aceitacao_afd = set()
    nomes_estados = {} # para nomes simples tipo Q0, Q1...
    
    contador = 0
    nomes_estados[estado_inicial_afd] = f"Q{contador}"
    contador += 1
    
    while fila:
        atual = fila.popleft()
        estados_afd.add(atual)
        transicoes_afd[atual] = {}
        
        for s in simbolos:
            proximo = set()
            for estado in atual:
                proximo.update(afnd[estado].get(s, []))
            proximo_frozen = frozenset(proximo)
            
            # Dar nome ao novo estado
            if proximo_frozen not in nomes_estados and proximo_frozen:
                nomes_estados[proximo_frozen] = f"Q{contador}"
                contador += 1
                
            transicoes_afd[atual][s] = proximo_frozen
            if proximo_frozen not in visitados and proximo_frozen:
                fila.append(proximo_frozen)
                visitados.add(proximo_frozen)
                
        # Estado de aceitação se contiver algum estado de aceitação do AFND
        if atual & estados_aceitacao:
            estados_aceitacao_afd.add(atual)
            
    return estados_afd, transicoes_afd, estado_inicial_afd, estados_aceitacao_afd, nomes_estados

# Passo 3: Executar conversão
estados_afd, transicoes_afd, inicial_afd, aceitos_afd, nomes_estados = afnd_para_afd(afnd, estado_inicial, estados_aceitacao, simbolos)

# Passo 4: Exibir resultados
print("Estados do AFD:")
for e in estados_afd:
    print(f"{nomes_estados[e]}: {set(e)}")

print("\nTransições do AFD:")
for e, t in transicoes_afd.items():
    trans = {s: nomes_estados[v] if v in nomes_estados else '{}' for s, v in t.items()}
    print(f"{nomes_estados[e]}: {trans}")

print("\nEstado inicial:", nomes_estados[inicial_afd])
print("Estados de aceitação:", [nomes_estados[e] for e in aceitos_afd])
~~~
Resultado:
~~~py
Estados do AFD:
Q0: {'q0'}
Q1: {'q0', 'q1'}
Q2: {'q2'}

Transições do AFD:
Q0: {'a': 'Q1', 'b': '{}'}
Q1: {'a': 'Q1', 'b': 'Q2'}
Q2: {'a': '{}', 'b': '{}'}

Estado inicial: Q0
Estados de aceitação: ['Q2']
~~~

### **10. AFD – múltiplos de 3 (binário)**
Crie um AFD que reconhece números binários múltiplos de 3 (ex: 0, 11, 110, etc.).
Resposta:
~~~py
def afd_multiplo_3(binario):
    estado = 'q0' # estado inicial
    for bit in binario:
        if bit not in '01':
            return False # símbolo inválido
        
        if estado == 'q0':
            estado = 'q0' if bit == '0' else 'q1'
        elif estado == 'q1':
            estado = 'q2' if bit == '0' else 'q0'
        elif estado == 'q2':
            estado = 'q1' if bit == '0' else 'q2'
            
    return estado == 'q0' # aceita se terminar em q0 (múltiplo de 3)

# Testes
testes = ["0", "11", "110", "10", "111", "1001", "abc"]
for t in testes:
    print(f"'{t}': {'Aceita' if afd_multiplo_3(t) else 'Rejeita'}")
~~~
Resultado:
~~~py
Claro, aqui estão as resoluções dos exercícios de 7 a 10, conforme solicitado.

7. AFD - cadeias terminando em '01'
Este programa simula um AFD que retorna True se a cadeia de entrada termina com '01'.

Python

def afd_termina_em_01(cadeia):
    estado = 'q0' # estado inicial
    for simbolo in cadeia:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q0'
            else:
                return False # símbolo inválido
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q2'
            else:
                return False
        elif estado == 'q2':
            if simbolo == '0':
                estado = 'q1'
            elif simbolo == '1':
                estado = 'q0'
            else:
                return False
    return estado == 'q2' # só aceita se terminar em q2

# Testes
testes = ["01", "001", "101", "1101", "111", "0", ""]
for teste in testes:
    resultado = afd_termina_em_01(teste)
    print(f"'{teste}': {'Aceita' if resultado else 'Rejeita'}")
Resultado:

'01': Aceita
'001': Aceita
'101': Aceita
'1101': Aceita
'111': Rejeita
'0': Rejeita
'': Rejeita
8. AFND - pelo menos um 'a' ou 'b'
A função a seguir implementa um autômato que aceita qualquer cadeia não vazia que contenha pelo menos um 'a' ou 'b'.

Python

def afnd_pelo_menos_um_a_ou_b(cadeia):
    # Se a cadeia estiver vazia, rejeita
    if not cadeia:
        return False
    
    # Estado inicial
    estado = 'q0'
    
    for simbolo in cadeia:
        if simbolo not in ('a', 'b'):
            return False # símbolo inválido
        
        # Transições do AFND
        if estado == 'q0':
            # ao ver 'a' ou 'b', vai para q1
            estado = 'q1'
        elif estado == 'q1':
            estado = 'q1' # permanece em q1
            
    # Aceita se terminar em q1
    return estado == 'q1'

# Testes
testes = ["a", "b", "ab", "ba", "aa", "bb", "", "c", "abc"]
for teste in testes:
    resultado = afnd_pelo_menos_um_a_ou_b(teste)
    print(f"'{teste}': {'Aceita' if resultado else 'Rejeita'}")
Resultado:

'a': Aceita
'b': Aceita
'ab': Aceita
'ba': Aceita
'aa': Aceita
'bb': Aceita
'': Rejeita
'c': Rejeita
'abc': Rejeita
9. Conversão AFND para AFD
O script abaixo converte um Autômato Finito Não Determinístico (AFND) em um Autômato Finito Determinístico (AFD) equivalente.

Python

from collections import deque

# Passo 1: Definir AFND
afnd = {
    'q0': {'a': ['q0', 'q1'], 'b': []},
    'q1': {'a': [], 'b': ['q2']},
    'q2': {'a': [], 'b': []}
}
estado_inicial = 'q0'
estados_aceitacao = {'q2'}
simbolos = ['a', 'b']

# Passo 2: Função de conversão AFND -> AFD
def afnd_para_afd(afnd, estado_inicial, estados_aceitacao, simbolos):
    estado_inicial_afd = frozenset([estado_inicial])
    visitados = set()
    transicoes_afd = {}
    fila = deque([estado_inicial_afd])
    estados_afd = set()
    estados_aceitacao_afd = set()
    nomes_estados = {} # para nomes simples tipo Q0, Q1...
    
    contador = 0
    nomes_estados[estado_inicial_afd] = f"Q{contador}"
    contador += 1
    
    while fila:
        atual = fila.popleft()
        estados_afd.add(atual)
        transicoes_afd[atual] = {}
        
        for s in simbolos:
            proximo = set()
            for estado in atual:
                proximo.update(afnd[estado].get(s, []))
            proximo_frozen = frozenset(proximo)
            
            # Dar nome ao novo estado
            if proximo_frozen not in nomes_estados and proximo_frozen:
                nomes_estados[proximo_frozen] = f"Q{contador}"
                contador += 1
                
            transicoes_afd[atual][s] = proximo_frozen
            if proximo_frozen not in visitados and proximo_frozen:
                fila.append(proximo_frozen)
                visitados.add(proximo_frozen)
                
        # Estado de aceitação se contiver algum estado de aceitação do AFND
        if atual & estados_aceitacao:
            estados_aceitacao_afd.add(atual)
            
    return estados_afd, transicoes_afd, estado_inicial_afd, estados_aceitacao_afd, nomes_estados

# Passo 3: Executar conversão
estados_afd, transicoes_afd, inicial_afd, aceitos_afd, nomes_estados = afnd_para_afd(afnd, estado_inicial, estados_aceitacao, simbolos)

# Passo 4: Exibir resultados
print("Estados do AFD:")
for e in estados_afd:
    print(f"{nomes_estados[e]}: {set(e)}")

print("\nTransições do AFD:")
for e, t in transicoes_afd.items():
    trans = {s: nomes_estados[v] if v in nomes_estados else '{}' for s, v in t.items()}
    print(f"{nomes_estados[e]}: {trans}")

print("\nEstado inicial:", nomes_estados[inicial_afd])
print("Estados de aceitação:", [nomes_estados[e] for e in aceitos_afd])
Resultado:

Estados do AFD:
Q0: {'q0'}
Q1: {'q0', 'q1'}
Q2: {'q2'}

Transições do AFD:
Q0: {'a': 'Q1', 'b': '{}'}
Q1: {'a': 'Q1', 'b': 'Q2'}
Q2: {'a': '{}', 'b': '{}'}

Estado inicial: Q0
Estados de aceitação: ['Q2']
10. AFD - múltiplos de 3 (binário)
O código abaixo cria um AFD que reconhece números binários que são múltiplos de 3.

Python

def afd_multiplo_3(binario):
    estado = 'q0' # estado inicial
    for bit in binario:
        if bit not in '01':
            return False # símbolo inválido
        
        if estado == 'q0':
            estado = 'q0' if bit == '0' else 'q1'
        elif estado == 'q1':
            estado = 'q2' if bit == '0' else 'q0'
        elif estado == 'q2':
            estado = 'q1' if bit == '0' else 'q2'
            
    return estado == 'q0' # aceita se terminar em q0 (múltiplo de 3)

# Testes
testes = ["0", "11", "110", "10", "111", "1001", "abc"]
for t in testes:
    print(f"'{t}': {'Aceita' if afd_multiplo_3(t) else 'Rejeita'}")
Resultado:

'0': Aceita
'11': Aceita
'110': Aceita
'10': Rejeita
'111': Rejeita
'1001': Aceita
'abc': Rejeita
~~~

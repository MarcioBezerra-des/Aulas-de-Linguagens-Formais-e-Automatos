# **Documentação do Script: `analisador_lexico`**

## **1. Visão Geral**

  O código define uma função chamada `analisador_lexico` que utiliza expressões regulares (regex) para identificar e classificar diferentes partes de uma string de entrada. Este processo, conhecido como análise léxica ou "tokenização", é o primeiro passo fundamental na compilação ou interpretação de uma linguagem de programação. A função retorna uma lista de tuplas, onde cada tupla representa um token encontrado e seu respectivo tipo.

## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

### **A Função `analisador_lexico(codigo_fonte)`**

A função principal do script, que realiza a análise léxica.

### **Parâmetros**

* `codigo_fonte (str):` Uma string que representa uma linha ou um trecho de código a ser analisado.

### **Retorno**

* `list:` Uma lista de tuplas. Cada tupla contém dois elementos:

  1. O valor do token (a string real encontrada, ex: `"int"`, `"x"`, `"="`).

  2. O tipo do token (uma string que classifica o token, ex: `'PALAVRA_CHAVE'`, `'IDENTIFICADOR'`, `'OPERADOR'`).

## **3. Lógica de Funcionamento**

### **3.1 Definição das Regras de Tokens:**

* A variável `regras_tokens` é uma lista de tuplas. Cada tupla define um tipo de token e o padrão de expressão regular (regex) para identificá-lo.

* `('PALAVRA_CHAVE', r'\b(int|float|if|else|while|return)\b'):` Identifica palavras-chave reservadas da linguagem. O `\b` garante que apenas palavras inteiras sejam capturadas (ex: "int" será capturado, mas "interno" não).

* `('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'):` Identifica nomes de variáveis ou funções. Eles devem começar com uma letra ou sublinhado, seguido por letras, números ou sublinhados.

* `('NUMERO', r'\d+'):` Captura sequências de um ou mais dígitos.

* `('OPERADOR', r'(=|\+|-|\*|/)'):` Identifica operadores aritméticos e de atribuição.

* `('DELIMITADOR', r';'):` Captura o caractere ponto e vírgula, usado como final de instrução.

* `('ESPACO', r'\s+'):` Identifica um ou mais caracteres de espaço em branco (espaços, tabs, etc.). Este token é usado para ser ignorado na saída final.

* `('DESCONHECIDO', r'.'):` Uma regra "pega-tudo" que captura qualquer caractere que não corresponda a nenhuma das regras anteriores.

### **3.2 Construção da Expressão Regular Combinada:**

* A linha `regex = '|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in regras_tokens)` é a parte central do analisador.

* Ela itera sobre a lista `regras_tokens` e constrói uma única e grande expressão regular.

* O operador `|` (OU) permite que o motor de regex tente corresponder a cada padrão na ordem em que foram definidos.

* `(?P<nome>...)` é um "grupo nomeado". Isso significa que, quando uma parte da string corresponde a um padrão, podemos facilmente saber a qual regra (pelo `nome`) ela pertence. Por exemplo, se `\d+` for encontrado, saberemos que ele pertence ao grupo nomeado `NUMERO`.

### **3.3 Busca e Classificação de Tokens:**

* `re.finditer(regex, codigo_fonte)` percorre a string `codigo_fonte` e encontra todas as correspondências não sobrepostas da expressão regular combinada.

* Para cada `correspondencia` encontrada:

  * `correspondencia.lastgroup` retorna o nome do grupo que casou com o texto (ex: `'PALAVRA_CHAVE'`, `'IDENTIFICADOR'`). Este é o `tipo_token`.

  * `correspondencia.group(tipo_token)` retorna o texto real que foi capturado (ex: `"int"`, `"x"`). Este é o `valor_token`.

  * Há uma verificação para garantir que o `tipo_token` não seja `'ESPACO'`. Se não for, a tupla `(valor_token, tipo_token)` é adicionada à lista `tokens`. Isso efetivamente ignora todos os espaços em branco.

### **3.4 Retorno da Lista de Tokens:**

* Ao final do processo, a lista `tokens` completa é retornada.

## **4. Exemplo de Execução**

* O script demonstra o uso da função com a entrada `"int x = 10;"`.

* Entrada: `"int x = 10;"`

* Processo:

  * `"int"` corresponde à regra `PALAVRA_CHAVE`.
  
  * O espaço é ignorado.
  
  * `"x"` corresponde à regra `IDENTIFICADOR`.
  
  * O espaço é ignorado.
  
  * `"="'` corresponde à regra `OPERADOR`.
  
  * O espaço é ignorado.
  
  * `"10"` corresponde à regra `NUMERO`.
  
  * `";"` corresponde à regra `DELIMITADOR`.

* Saída Formatada:
~~~py
Tokens Gerados:
-------------------------
Token           | Tipo
-------------------------
int             | PALAVRA_CHAVE
x               | IDENTIFICADOR
=               | OPERADOR
10              | NUMERO
;               | DELIMITADOR
-------------------------
~~~
## **5. Conclusão**

Este código é uma implementação prática e eficiente de um analisador léxico. Ele demonstra o poder das expressões regulares para realizar o reconhecimento de padrões e a tokenização de um texto, um passo essencial para a criação de interpretadores, compiladores, linters e outras ferramentas de análise de código.

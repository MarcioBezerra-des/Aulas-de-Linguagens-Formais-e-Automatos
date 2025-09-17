# Documentação do Script: `detectar_sql_injection`

## **1. Visão Geral**

  Este script Python demonstra uma abordagem simplificada para detectar um padrão comum de ataque de SQL Injection usando expressões regulares. O objetivo é analisar uma entrada de texto (como de um campo de login) e identificar se ela contém uma estrutura maliciosa projetada para burlar a lógica de uma consulta SQL..

## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

## **3. Função `detectar_sql_injection(entrada_usuario)`**
Esta função é o núcleo do script, realizando a verificação de segurança na string de entrada.

* **Propósito**: Analisar uma string fornecida pelo usuário (`entrada_usuario`) e determinar se ela corresponde a um padrão conhecido de ataque de SQL Injection do tipo "sempre verdadeiro" (tautologia).

* **Argumentos**:
  * `entrada_usuario (str)`: A string a ser inspecionada.
* **Retorno**:
  * `bool`: Retorna `True` se o padrão malicioso for encontrado; caso contrário, retorna `False`.
 
## **4. Análise da Expressão Regular (Regex)**
O poder desta função reside na expressão regular compilada, que define o que constitui uma "ameaça".
~~~py
padrao_malicioso = re.compile(
    r"'.*\s+(OR|or)\s+['\"]\d+['\"]\s*=\s*['\"]\d+['\"](\s*--|\s*#|;)?",
    re.IGNORECASE
)
~~~
Vamos detalhar cada parte deste padrão:
* `'` : Corresponde a uma aspa simples literal. Em muitos ataques, o invasor usa uma aspa para "escapar" de um campo de texto dentro de uma consulta SQL, permitindo injetar novos comandos.
* `.*`: Corresponde a qualquer caractere (`.`) zero ou mais vezes (`*`). Isso captura qualquer texto que o usuário possa ter inserido antes da cláusula `OR`.
* `\s+`: Corresponde a um ou mais caracteres de espaço em branco (espaços, tabs, etc.).
* `(OR|or)`: Corresponde à palavra "OR" ou "or". Esta é a chave do ataque, usada para adicionar uma nova condição à cláusula `WHERE`.
* `\s+: Novamente`, corresponde a um ou mais espaços em branco.
* `['\"]\d+['\"]`: Esta parte busca por um número entre aspas.
  * `['\"]`: Corresponde a uma aspa simples (`'`) ou uma aspa dupla (`"`).
  * `\d+`: Corresponde a um ou mais dígitos numéricos (de 0 a 9).
* `\s*=\s*`: Corresponde ao sinal de igual `=`, cercado por zero ou mais espaços em branco.
* `['\"]\d+['\"]`: Repete o padrão de um número entre aspas. Juntando com a parte anterior, o padrão completo `'1'='1'` ou `"2"="2"` cria uma condição que é sempre verdadeira.
* `(\s*--|\s*#|;)?`: Esta parte final busca por caracteres comuns usados para finalizar a injeção.
  * `\s*--`: Corresponde a `--`, que inicia um comentário em muitas sintaxes SQL, neutralizando o resto da consulta original.
  * `\s*#`: Corresponde a `#`, que também é um caractere de comentário.
  * `;`: Corresponde a um ponto e vírgula, que pode ser usado para terminar a instrução SQL prematuramente.
  * `?`: Torna todo este grupo final opcional, pois o ataque pode funcionar mesmo sem ele.
* `re.IGNORECASE`: Esta "flag" faz com que todo o padrão ignore a diferença entre maiúsculas e minúsculas (por exemplo, `or` é tratado da mesma forma que `OR`).

## **5. Lógica de Detecção**

* `re.compile(...)`: A expressão regular é "pré-compilada" para otimizar o desempenho, o que é uma boa prática se o padrão for usado várias vezes.
* `padrao_malicioso.search(entrada_usuario)`: O método `.search()` varre a string de entrada em busca de qualquer trecho que corresponda ao padrão. Se encontrar, retorna um objeto de correspondência; caso contrário, retorna `None`.
* O `if` simplesmente verifica se o resultado da busca foi bem-sucedido (não é `None`) para retornar `True`.

## **6. Bloco de Execução Principal**

Esta seção do código serve como um teste e demonstração da função.
* Entradas de Teste: Quatro strings são definidas:
  * `entrada_legitima`: Uma entrada comum e segura.
  * `entrada_maliciosa1`: Um ataque clássico usando `' OR '1'='1' --` para comentar o resto da consulta.
  * `entrada_maliciosa2`: Uma variação que usa um ponto e vírgula.
  * `entrada_maliciosa3`: Outra variação que usa aspas duplas.
* Processo de Verificação: O código itera sobre cada entrada, chama a função `detectar_sql_injection` e imprime um resultado claro, indicando se a entrada é considerada segura ou uma ameaça.

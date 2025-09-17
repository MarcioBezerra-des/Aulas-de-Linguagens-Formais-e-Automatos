# Documentação do Script: `encontrar_genes`

## **1. Visão Geral**

Este script Python foi projetado para identificar sequências de genes codificantes simples dentro de uma string que representa uma fita de DNA. Ele utiliza o módulo de expressões regulares (`re`) do Python para encontrar padrões que correspondam a uma estrutura genética básica: um códon de início, seguido por uma sequência de códons, e finalizado por um códon de parada.

## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

## **1. Função encontrar_genes`(sequencia_dna)`**

Esta é a função principal do script, responsável por realizar a busca pelos genes.

* Propósito: Localizar e extrair todas as substrings que se parecem com um gene, com base em um padrão pré-definido.

* Argumentos:
  * `sequencia_dna` (str): Uma string contendo a sequência de DNA a ser analisada (composta por 'A', 'T', 'C', 'G').
* Retorno:
  * `list:` Uma lista de tuplas. Cada tupla contém as partes do gene capturadas pela expressão regular (especificamente, a sequência de códons intermediários e o códon de parada).

## **2. Análise da Expressão Regular (Regex)**

A "inteligência" da busca está na expressão regular definida:
~~~py
padrao_gene = r'ATG([ATCG]{3})+(TAA|TAG|TGA)'
~~~

vamos quebrar essa expressão em partes:
* `ATG:` Esta parte corresponde exatamente à sequência literal "ATG". Este é o códon de início mais comum, que sinaliza o começo de um gene.
* `([ATCG]{3})+`: Esta é a parte central do gene.
  * `[ATCG]`: Define uma classe de caracteres. A correspondência será com qualquer um dos caracteres dentro dos colchetes: 'A', 'T', 'C' ou 'G'.
  * `{3}`: É um quantificador que exige que a classe de caracteres anterior `([ATCG])` se repita exatamente 3 vezes. Juntos, `[ATCG]{3}` definem um códon (um trio de nucleotídeos).
  * `(...)`: Os parênteses criam um grupo de captura. Isso significa que a parte da string que corresponder a este padrão será "salva" separadamente.
  * `+`: É um quantificador que significa "uma ou mais vezes". Portanto, `([ATCG]{3})+` corresponde a uma ou mais sequências de códons.
* `(TAA|TAG|TGA)`: Esta parte corresponde aos códons de parada.
  * `|`: Atua como um operador "OU" (OR). A expressão corresponderá a 'TAA', 'TAG', ou 'TGA'.
  * `(...)`: Os parênteses criam um segundo grupo de captura, que salvará qual dos três códons de parada foi encontrado.
## **3. Bloco de Execução Principal**
Esta seção do código demonstra como usar a função encontrar_genes e como processar seus resultados.

### **3.1 Inicialização**
~~~~py
# Exemplo de uma sequência de DNA
dna = "CGATGCGTATGCGTACGTAGCGCATTGATGCCCGGGAAATAGCTAG"
~~~~
Uma sequência de DNA de exemplo é definida para testar a função.

### **3.2 Chamada da Função e Verificação**
~~~~py
genes = encontrar_genes(dna)
if genes:
    ...
else:
    print("Nenhum gene com o padrão especificado foi encontrado.")
~~~~
A função é chamada com o DNA de exemplo. O `if genes`: verifica se a lista retornada não está vazia, ou seja, se pelo menos um gene foi encontrado.

### **3.3 Processamento e Impressão dos Resultados**
~~~~py
print(f"Foram encontrados {len(genes)} gene(s) potencial(is):")
padrao_gene = r'(ATG(?:[ATCG]{3})+(?:TAA|TAG|TGA))'
matches = re.finditer(padrao_gene, dna)
for i, match in enumerate(matches, 1):
    print(f"Gene {i}: {match.group(0)}")
~~~~
Esta parte é crucial para entender a saída. A primeira chamada a `encontrar_genes` com `re.findall` retorna apenas os grupos de captura, não a correspondência completa. Por exemplo, para o gene "ATGCGTTAG", `re.findall` retornaria `[('CGT', 'TAG')]`.

Para obter a sequência completa do gene ("ATGCGTTAG"), o código executa uma nova busca usando `re.finditer`.

* `re.finditer`: Este método é mais poderoso que `findall` porque retorna um "iterador" de objetos de correspondência (`match objects`), em vez de apenas strings. Cada objeto de correspondência contém informações detalhadas sobre a correspondência, incluindo a string completa.
* Regex Modificada: A expressão `r'(ATG(?:[ATCG]{3})+(?:TAA|TAG|TGA))'` é ligeiramente diferente. O `?`: dentro de um grupo `(...)` o transforma em um grupo de não-captura. Isso é feito para que o `finditer` capture apenas um grupo: o gene inteiro.
* `match.group(0)`: Para cada correspondência encontrada pelo `finditer`, `match.group(0)` retorna a substring inteira que correspondeu ao padrão, que é exatamente o que queremos imprimir: o gene completo, do códon de início ao códon de parada.

### **3.4 Saída do Exemplo**
Com a sequência de DNA fornecida, a saída do script será:

~~~py
Sequência de DNA de entrada:
CGATGCGTATGCGTACGTAGCGCATTGATGCCCGGGAAATAGCTAG

Foram encontrados 2 gene(s) potencial(is):
Gene 1: ATGCGTATGCGTACGTAG
Gene 2: ATGCCCGGGAAATAG
~~~

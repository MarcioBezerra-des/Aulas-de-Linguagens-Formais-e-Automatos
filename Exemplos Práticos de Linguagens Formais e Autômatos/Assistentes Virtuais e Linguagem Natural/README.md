# **Documentação do Script: `chatbot_parser`**

## **1. Visão Geral**

  O código define uma função chamada `chatbot_parser` que recebe uma string de texto como entrada. Essa entrada é processada e validada com base em um conjunto de regras gramaticais simples, que esperam uma estrutura de "Comando" seguido de "Objeto". Se a entrada for válida, uma mensagem de sucesso é retornada; caso contrário, uma mensagem de erro é exibida.

## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

### **A Função `chatbot_parser(entrada)`**

A função principal do script, responsável por toda a lógica de processamento e validação.

### **Parâmetros**

* `entrada (str):` Uma string de texto que representa o comando do usuário a ser analisado.

### **Retorno**

* `str`  Uma string contendo o resultado da análise, que pode ser uma confirmação da ação executada ou uma mensagem de erro.

## **3. Lógica de Funcionamento**

O funcionamento do parser pode ser dividido nas seguintes etapas:

### **3.1 Definição da Gramática:**

* Duas listas, `comandos_validos` e `objetos_validos`, são definidas para estabelecer o vocabulário permitido pela gramática.

  * `comandos_validos = ["ligue", "desligue", "abra"]`

  * `objetos_validos = ["luz", "portão", "música"]`

* Isso significa que o parser só reconhecerá esses termos específicos como comandos e objetos válidos.

### **3.2 Normalização e Tokenização:**

* A string de `entrada` é convertida para letras minúsculas com o método `.lower()` para garantir que a análise não seja sensível a maiúsculas e minúsculas (ex: "Ligue" e "ligue" são tratados da mesma forma).

* Em seguida, a entrada é dividida em uma lista de palavras (tokens) usando o método `.split()`, que separa a string pelos espaços em branco.

### **3.3 Validação da Estrutura:**

* O parser verifica se a lista de palavras contém exatamente dois elementos `(len(palavras) != 2)`.

* Esta é a regra estrutural fundamental da gramática: a entrada deve ser composta por exatamente duas palavras, um "Comando" e um "Objeto". Se a entrada tiver mais ou menos de duas palavras (ex: "abra o portão"), ela é considerada inválida.

### **3.4 Análise Léxica e Semântica:**

* Se a estrutura for válida (duas palavras), a primeira palavra é atribuída à variável `comando` e a segunda à variável `objeto`.

* O código então verifica se a palavra em `comando` existe na lista `comandos_validos` e se a palavra em `objeto` existe na lista `objetos_validos`.

### **3.5 Geração da Saída:**

* Se ambos, comando e objeto, forem válidos: Uma string formatada é retornada, simulando a execução da ação. Ex: `"Ação executada: Ligue o(a) luz."`.

* Se o comando ou o objeto forem inválidos: Uma mensagem de erro genérica é retornada: `"Erro: Comando ou objeto inválido."`.

* Se a estrutura for inválida (diferente de duas palavras): Uma mensagem de erro específica é retornada: `"Erro: Comando não reconhecido. Use o formato: 'Comando Objeto'."`.

## **4. Exemplos de Execução**

O script demonstra o comportamento do parser com quatro exemplos distintos:

### **4.1 `entrada1 = "ligue luz"`**

* Análise: "ligue" é um comando válido e "luz" é um objeto válido. A estrutura tem duas palavras.

* Saída: `Ação executada: Ligue o(a) luz.` (Sucesso)

### **`4.2 entrada2 = "abra o portão`"**

* Análise: A entrada é dividida em `['abra', 'o', 'portão']`. O tamanho é 3, o que viola a regra de estrutura da gramática.

* Saída: `Erro: Comando não reconhecido. Use o formato: 'Comando Objeto'.` (Falha na estrutura)

### **`4.3 entrada3 = "desligue música"`**

* Análise: "desligue" é um comando válido e "música" é um objeto válido. A estrutura tem duas palavras.

* Saída: `Ação executada: Desligue o(a) música.` (Sucesso)

### **`4.4 entrada4 = "toque som`"**

* Análise: A estrutura com duas palavras é válida. No entanto, "toque" não está em `comandos_validos` e "som" não está em `objetos_validos`.

* Saída: `Erro: Comando ou objeto inválido.` (Falha na validação dos termos)

### **`4.5 Saída Formatada`**

~~~py
Entrada: "ligue luz"
Saída: Ação executada: Ligue o(a) luz.

Entrada: "abra o portão"
Saída: Erro: Comando não reconhecido. Use o formato: 'Comando Objeto'.

Entrada: "desligue música"
Saída: Ação executada: Desligue o(a) música.

Entrada: "toque som"
Saída: Erro: Comando ou objeto inválido.
~~~

## **5. Conclusão**

Este código é um exemplo claro e simples de um parser de análise sintática descendente recursiva (Top-Down Parser). Ele utiliza um conjunto fixo de regras gramaticais para validar e interpretar comandos. Embora simples, ele ilustra os conceitos fundamentais de tokenização, validação de gramática e análise de entrada que são a base para chatbots e compiladores mais complexos.

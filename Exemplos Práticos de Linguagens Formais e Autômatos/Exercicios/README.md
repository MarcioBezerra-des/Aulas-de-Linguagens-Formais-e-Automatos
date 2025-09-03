# **Exercícios de Teoria da Computação: Autômatos e a Hierarquia de Chomsky**

  Este repositório contém uma série de exercícios sobre conceitos fundamentais da Teoria da Computação, com foco na Hierarquia de Chomsky, Máquinas de Turing e Autômatos Finitos. Para cada questão teórica, uma solução algorítmica em Python é fornecida para ilustrar o conceito na prática.

  O objetivo é servir como material de estudo, conectando a teoria abstrata com exemplos de código concretos e funcionais.

## **Tópicos Abordados**
* Hierarquia de Chomsky: Classificação de linguagens formais (Regulares, Livres de Contexto, Sensíveis ao Contexto, Recursivamente Enumeráveis).
* Modelos Computacionais: Autômatos Finitos Determinísticos (AFD), Autômatos com Pilha e Máquinas de Turing.
* Poder Computacional: Comparação entre os diferentes modelos de autômatos.
* Limites da Computação: Noções sobre o que pode ou não ser computado.

## **Lista de Exercícios**

~~~
Para cada resposta deve ser desenvolver um exemplo da resposta em solução algorítmica em Pyton  

Exercícios:  

A Hierarquia de Chomsky, proposta pelo linguista Noam Chomsky em 1956, é uma classificação formal das linguagens com base no tipo de regras gramaticais que elas utilizam. Essa hierarquia divide as linguagens formais em quatro classes principais, cada uma reconhecida por um tipo específico de autômato: (1) Linguagens Regulares, reconhecidas por Autômatos Finitos; (2) Linguagens Livres de Contexto, reconhecidas por Autômatos com Pilha; (3) Linguagens Sensíveis ao Contexto, reconhecidas por Máquinas Linearmente Limitadas; e (4) Linguagens Recursivamente Enumeráveis, reconhecidas por Máquinas de Turing. Essa classificação é fundamental para a teoria da computação, pois estabelece os limites do que pode ser computado por diferentes modelos formais e serve de base para a construção de linguagens de programação e compiladores.

Referência bibliográfica: HOPCROFT, J. E.; MOTWANI, R.; ULLMAN, J. D. Introduction to Automata Theory, Languages, and Computation. 3. ed. Boston: Pearson/Addison Wesley, 2006.

1.Qual das opções não faz parte da hierarquia de Chomsky?

  A) Linguagens regulares
  B) Linguagens livres de contexto
  C) Linguagens orientadas a objetos (Correto)
  D) Linguagens recursivamente enumeráveis

2.Qual modelo reconhece linguagens regulares?

  A) Autômato de Pilha
  B) Máquina de Turing
  C) AFD (Correto)
  D) Máquina Linearmente Limitada

A Máquina de Turing, idealizada por Alan Turing em 1936, é um modelo matemático abstrato que define formalmente o conceito de computação. Essa máquina consiste em uma fita infinita dividida em células (que representam a memória), um cabeçote de leitura e escrita que se move pela fita, e uma tabela de regras (função de transição) que determina suas ações com base no estado atual e no símbolo lido. A Máquina de Turing é fundamental na teoria da computação, pois demonstra que certos problemas são computáveis apenas se houver um algoritmo para resolvê-los. Ela é considerada tão poderosa quanto qualquer computador moderno em termos de capacidade de cálculo, sendo a base para a definição do que é uma função computável.

Referência bibliográfica:
TURING, A. M. On Computable Numbers, with an Application to the Entscheidungsproblem. Proceedings of the London Mathematical Society, v. 42, n. 2, p. 230–265, 1936.

3.A máquina de Turing é um modelo de:

  A) Processador lógico
  B) Computação universal (Correto)
  C) Otimização de tempo
  D) Busca recursiva
 
4.Qual linguagem não é regular?

  A) {a, aa, aaa}
  B) {aⁿbⁿ | n ≥ 0} (Correto)
  C) {ab}
  D) (ab)*

5.Qual modelo é mais poderoso?

  A) Autômato finito
  B) Autômato com pilha
  C) Máquina de Turing (Correto)
  D) Expressão regular

6.O Autômato com Pilha reconhece:

  A) Linguagens sensíveis ao contexto
  B) Linguagens livres de contexto (Correto)
  C) Linguagens regulares
  D) Linguagens naturais

A Máquina de Autômato Finito Determinístico (AFD) é um modelo matemático utilizado para representar e reconhecer linguagens regulares. Um AFD consiste em um conjunto finito de estados, um alfabeto de entrada, uma função de transição determinística, um estado inicial e um ou mais estados finais. Para cada símbolo de entrada e estado atual, a máquina realiza uma única transição, o que caracteriza seu comportamento determinístico. Os AFDs são amplamente utilizados em áreas como análise léxica de compiladores, validação de padrões (como expressões regulares) e modelagem de protocolos de comunicação. Sua simplicidade estrutural os torna ideais para aplicações em sistemas que exigem reconhecimento eficiente de padrões fixos e sequenciais.

Referência bibliográfica:
HOPCROFT, J. E.; MOTWANI, R.; ULLMAN, J. D. Introduction to Automata Theory, Languages, and Computation. 3. ed. Boston: Pearson/Addison Wesley, 2006.

7.Qual modelo usa uma pilha como memória auxiliar?

  A) AFD
  B) Máquina de Turing
  C) Autômato com Pilha (Correto)
  D) AFND

8.A hierarquia de Chomsky classifica linguagens com base:

  A) Na sua frequência de uso
  B) Em sua complexidade sintática (Correto)
  C) Em seu vocabulário
  D) Em seu uso computacional

 9.O autômato finito não pode reconhecer:

  A) Cadeias com número par de “a”
  B) Cadeias palíndromas (Correto)
  C) Cadeias com símbolos específicos
  D) Cadeias com padrões alternados

10.Qual o objetivo principal de estudar autômatos?

  A) Simular processadores modernos
  B) Compreender limites da computação (Correto)
  C) Criar linguagens naturais
  D) Substituir compiladores
~~~

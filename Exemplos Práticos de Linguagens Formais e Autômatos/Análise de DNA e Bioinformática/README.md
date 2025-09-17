5. Análise de DNA e Bioinformática
Expressões Regulares (ER) são ferramentas poderosas em bioinformática para encontrar padrões em sequências biológicas, como DNA, RNA e proteínas. Uma sequência de DNA pode ser representada como uma longa string de caracteres (A, T, C, G). As ER permitem aos cientistas localizar genes, sítios de ligação de proteínas e outras regiões de interesse.

Código de Exemplo: Identificação de Sequências de DNA
O código a seguir usa uma expressão regular para encontrar um padrão de gene codificante simples em uma sequência de DNA. O padrão busca um códon de início (ATG), seguido por qualquer número de códons de três letras, e terminando com um dos três códons de parada (TAA, TAG ou TGA).

Documentação do Código
padrao_gene: Esta é a expressão regular que define a estrutura de um gene simples:

ATG: Corresponde literalmente ao códon de início.

([ATCG]{3})+: Corresponde a um ou mais grupos (+) de exatamente três ({3}) caracteres do conjunto [ATCG]. Este é o corpo do gene.

(TAA|TAG|TGA): Corresponde a um dos três possíveis códons de parada. O | funciona como um "OU".

re.finditer: Este método é usado para encontrar todas as ocorrências do padrão na sequência de DNA. Ele retorna um iterador com objetos de correspondência, dos quais podemos extrair a sequência completa do gene encontrado usando .group(0).

Aplicação: A função pode escanear rapidamente longas sequências genômicas, automatizando uma tarefa que seria extremamente tediosa e propensa a erros se feita manualmente.

import re

def encontrar_genes(sequencia_dna):
   
    padrao_gene = r'ATG([ATCG]{3})+(TAA|TAG|TGA)'

    genes_encontrados = re.findall(padrao_gene, sequencia_dna)

    return genes_encontrados


dna = "CGATGCGTATGCGTACGTAGCGCATTGATGCCCGGGAAATAGCTAG"

print(f"Sequência de DNA de entrada:\n{dna}\n")
genes = encontrar_genes(dna)

if genes:
    print(f"Foram encontrados {len(genes)} gene(s) potencial(is):")
    for i, gene in enumerate(genes):
       
        padrao_gene = r'(ATG(?:[ATCG]{3})+(?:TAA|TAG|TGA))'
        matches = re.finditer(padrao_gene, dna)
        for i, match in enumerate(matches, 1):
             print(f"Gene {i}: {match.group(0)}")
else:
    print("Nenhum gene com o padrão especificado foi encontrado.")
import re

def detectar_sql_injection(entrada_usuario):
    
    padrao_malicioso = re.compile(
        r"'.*\s+(OR|or)\s+['\"]\d+['\"]\s*=\s*['\"]\d+['\"](\s*--|\s*#|;)?",
        re.IGNORECASE
    )

    if padrao_malicioso.search(entrada_usuario):
        return True
    return False

entrada_legitima = "admin"
entrada_maliciosa1 = "' OR '1'='1' --"
entrada_maliciosa2 = "qualquercoisa' or '1'='1';"
entrada_maliciosa3 = "x' OR \"2\"=\"2\""

print(f"Verificando entrada: \"{entrada_legitima}\"")
if detectar_sql_injection(entrada_legitima):
    print("Resultado: Ameaça detectada! Bloqueando a requisição.\n")
else:
    print("Resultado: Entrada segura.\n")


print(f"Verificando entrada: \"{entrada_maliciosa1}\"")
if detectar_sql_injection(entrada_maliciosa1):
    print("Resultado: Ameaça detectada! Bloqueando a requisição.\n")
else:
    print("Resultado: Entrada segura.\n")

print(f"Verificando entrada: \"{entrada_maliciosa2}\"")
if detectar_sql_injection(entrada_maliciosa2):
    print("Resultado: Ameaça detectada! Bloqueando a requisição.\n")
else:
    print("Resultado: Entrada segura.\n")
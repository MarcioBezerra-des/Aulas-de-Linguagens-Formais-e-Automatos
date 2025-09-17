6. Segurança da Informação e Firewalls
Firewalls de Aplicação Web (WAFs) e Sistemas de Detecção de Intrusão (IDS) usam reconhecimento de padrões para identificar tráfego malicioso. Um Autômato Finito (frequentemente implementado com expressões regulares) pode ser programado para detectar assinaturas de ataques conhecidos, como a Injeção de SQL.

Código de Exemplo: Detecção de Ataques SQL Injection
Este exemplo mostra uma função simples que simula como um firewall poderia usar uma expressão regular para verificar se uma entrada de usuário contém um padrão clássico de injeção de SQL.

Documentação do Código
padrao_malicioso: A expressão regular é projetada para ser flexível e detectar variações do ataque ' OR '1'='1'.

re.compile: Pré-compila a expressão regular para um desempenho mais eficiente se a função for chamada muitas vezes.

re.IGNORECASE: Torna a detecção insensível a maiúsculas e minúsculas (por exemplo, OR ou or).

padrao_malicioso.search(): Este método escaneia a string de entrada. Se o padrão for encontrado em qualquer lugar da string, ele retorna um objeto de correspondência (avaliado como True); caso contrário, retorna None (avaliado como False).

Simulação do Firewall: A função retorna um booleano que indica a presença da ameaça. Em um sistema real, um retorno True acionaria uma ação, como registrar o evento, alertar um administrador e bloquear o endereço IP do solicitante.

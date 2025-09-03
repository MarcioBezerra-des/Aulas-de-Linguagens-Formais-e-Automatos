# Documentação do Script: `validador_emails.py`

## **1. Visão Geral**

  O script `validador_emails.py` é uma ferramenta de linha de comando desenvolvida em Python para coletar e validar endereços de e-mail. Seu objetivo principal é garantir que até 5 e-mails únicos e com formato válido sejam inseridos pelo usuário.

## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

## **3. Como usar**

Para executar o script, siga os passos abaixo:

* Salve o código em um arquivo chamado validador_de_emails.py.
* Abra um terminal ou prompt de comando.
* Navegue até o diretório onde você salvou o arquivo.
* Execute o script com o seguinte comando:
  `python validador_de_emails.py`
* O programa solicitará que você digite os e-mails um por um. Após cadastrar 5 e-mails válidos e únicos, o programa será encerrado, exibindo a lista final.

## **4. Detalhamento do Código**

  O código é estruturado dentro de uma função principal para organização e clareza.

### **3.1 Importações**
```py
import re
```
* `import re:` Importa a biblioteca re, que é o módulo de expressões regulares do Python. Esta biblioteca é fundamental para realizar a validação do formato do e-mail.

### **3.2 Função validador_de_emails()**
~~~py
def validar_email():
~~~
Esta função encapsula toda a lógica do programa.

### **3.3 Variáveis Iniciais**
~~~py
emails_cadastrados = []
regex_validador = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
~~~

* `emails_cadastrados = []:` Inicializa uma lista vazia. Esta lista funcionará como um "array" para armazenar os e-mails que passarem em todas as validações.

* `regex_validador:` Uma variável do tipo raw string (indicada pelo r antes das aspas) que armazena o padrão da expressão regular. Este padrão define a estrutura de um e-mail válido:

  * `^[a-zA-Z0-9._%+-]+:` Início da string, seguido por um ou mais caracteres permitidos para o nome do e-mail.

  * `@:` O símbolo de "arroba".

  * `[a-zA-Z0-9.-]+:` O domínio (ex: "gmail", "outlook").

  * `\.:` Um ponto literal.

  * `[a-zA-Z]{2,}:` A extensão do domínio (ex: "com", "br", "org"), com no mínimo 2 caracteres.

  * `$:` Fim da string.
  
### **3.4 Loop Principal e Lógica de Validação**
~~~py
while len(emails_cadastrados) < 5:
        email_input = input(f"Digite o {len(emails_cadastrados) + 1}º e-mail e pressione Enter: ")

        if re.match(regex_validador, email_input):
            
            if email_input in emails_cadastrados:
                print("\x1b[31mEsse Email já existe\x1b[0m")
            else:
                emails_cadastrados.append(email_input)
                print("\x1b[32mEmail cadastrado com sucesso.\x1b[0m")
        else:
            print("\x1b[31mFormato de e-mail inválido. Tente novamente.\x1b[0m")
~~~

* `while len(emails_cadastrados) < 5:`: O coração do programa. Este laço `while` continua a execução enquanto o número de e-mails na lista for menor que 5.

* `input(...):` Exibe uma mensagem para o usuário e aguarda a digitação de um e-mail. O texto digitado é armazenado na variável `email_input.`

* `if re.match(...):` Utiliza a função `match()` da biblioteca `re` para comparar o início da string `email_input` com o padrão `regex_validador.` Se corresponder, o bloco de código interno é executado. Caso contrário, o `else` é acionado, informando que o formato é inválido.

* `if email_input in emails_cadastrados:`: Se o formato for válido, esta linha verifica se o e-mail já está presente na lista `emails_cadastrados`. Esta é uma maneira eficiente em Python de verificar a existência de um item em uma lista.

* `emails_cadastrados.append(email_input):` Se o e-mail for válido e não for uma duplicata, este comando o adiciona ao final da lista.

* `print("\x1b[...m ... \x1b[0m"):` Os códigos como `\x1b[31m` são sequências de escape ANSI usadas para exibir texto colorido no terminal, melhorando a experiência do usuário. `\x1b[31m` define a cor vermelha e `\x1b[32m` define a cor verde. `\x1b[0m` reverte para a cor padrão.

### **3.5 Finalização**
~~~py
    print("\n--- Cadastro Concluído ---")
    print("Os 5 e-mails cadastrados foram:")
    for email in emails_cadastrados:
        print(f"- {email}")
~~~
* Quando o loop while termina (após 5 e-mails serem cadastrados), estas linhas são executadas para informar ao usuário que o processo foi concluído e para exibir a lista final de e-mails cadastrados.
  
### **3.6. Ponto de Entrada do Script**
~~~py
if __name__ == "__main__":
    validador_de_emails()
~~~

* `if __name__ == "__main__":` Esta é uma construção padrão em Python. Ela verifica se o script está sendo executado diretamente pelo interpretador. Em caso afirmativo, a função `validador_de_emails()` é chamada. Isso evita que a função seja executada caso este arquivo seja importado como um módulo por outro script.
****

import re

def validar_email():

    emails_cadastrados = []

    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    print("Cadastro de Email (limite de 5 emails)")
    print('(Digite "sair" ou "exit" a qualquer momento para encerrar)')

    while len(emails_cadastrados) < 5:
        email_input = input(f"Digite o email {len(emails_cadastrados) + 1}º e-mail e pressione Enter: ")

        if email_input.lower() == 'sair' or email_input.lower() == 'exit':
            break

        if re.match(regex, email_input):
            if email_input in emails_cadastrados:
                print("\x1b[31mEmail já cadastrado. Tente novamente.\x1b[0m")
            else:
                emails_cadastrados.append(email_input)
                print("\x1b[32mEmail cadastrado com sucesso!\x1b[0m")
        else:
            print("\x1b[31mEmail inválido. Tente novamente.\x1b[0m")
        
    print("\n Cadastro de emails concluído.")
    print("Emails cadastrados:")
    for email in emails_cadastrados:
        print(f"- {email}")
        
if __name__ == "__main__":
    validar_email()
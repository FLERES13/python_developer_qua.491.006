import classe as c
import os

limpar = lambda: os.system("cls" if os.name =="nt" else "clear")

def main():

    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    print("Entre com os dados do usuário:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereco: ").strip().title()

    limpar()


    print("Entre com os dados da empresa:\n")

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereco da empresa: ").strip().title()

    limpar()
    print("Dados do usuário: ")
    usuario.exibir_dados()
    print("Dados da empresa: ")
    empresa.exibir_dados()




if __name__ == "__main__":
    main()






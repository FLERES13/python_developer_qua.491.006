import classes as c 
import os 

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")



    print("Insira os dados do usuário:\n")


    usuario.nome = input("Informe o nome").strip().title()
    usuario.cpf = input("Informe o cpf").strip()
    usuario.telefone = input("Informe o telefone").strip()
    usuario.endereco = input("Informe o endereco").strip().title()


    limpar()


    empresa.nome_fantasia = input("Infome o nome da empresa: ").strip().title()
    empresa.cnpj = input("Infomre o CNPJ da empresa: ").strip()
    empresa.telefone =  input("Informe o telefone da empresa ")


if __name__== "__main__":
    main()    
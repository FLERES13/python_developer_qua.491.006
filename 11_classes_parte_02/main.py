import PessoaFisica
import PessoaJuridica
import os 

limpar =  lambda: os.system("cls" if os.name == "nt" else "clear")


def main():
    usuario = PessoaFisica.PessoaFisica(
        email="", telefone="", endereco="",
        nome="", cpf="", idade=0
    )
    empresa = PessoaJuridica.PessoaJuridica(
        email="", telefone="", endereco="", razao_social="", nome="", cnpj="",

    )

    print("Informe os dados do usuario: \n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu cpf: ").strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereco: ").strip()
    

    limpar()


    print("Informe os dados da empresa: \n")
    usuario.razao_social = input("Informe a razao social : ").strip()
    usuario.nome_fantasia = input("Informe o nome da razao social: ").strip()
    usuario.cnpj = input("Informe o cnpj: ")
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.telefone = input("Informe o telefone da empresa : ").strip()
    usuario.endereco = input("Informe seu endereco da empresa : ").strip()

    limpar()


    print(usuario)
    print(empresa)


    if __name__ == "__main__":
        main()
                            



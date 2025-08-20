from pessoa import Pessoa

def main():
    usuario = Pessoa("", "", "", 0, 0.0)

    usuario.set_nome(input("Informe seu nome: "))
    usuario.set_email(input("Informe seu email: "))
    usuario.set_cpf(input("Informe seu cpf: "))
    usuario.set_idade(int(input("Informe sua idade: ")))
    usuario.set_altura(float(input("Informe sua altura: ").replace(",", ".")))

    print("\n--- Dados do Usuário ---")
    print(usuario)

if __name__ == "__main__":
    main()

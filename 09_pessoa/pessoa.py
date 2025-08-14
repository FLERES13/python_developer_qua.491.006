class Pessoa:
    def __init__(self, nome: str, email: str, cpf: str, idade: int, altura: float):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura

    # GETTERS
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_cpf(self):
        return self.__cpf

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    # SETTERS
    def set_nome(self, nome: str):
        self.__nome = nome.strip().title()

    def set_email(self, email: str):
        self.__email = email.strip().lower()

    def set_cpf(self, cpf: str):
        self.__cpf = cpf.strip()

    def set_idade(self, idade: int):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade inválida!")

    def set_altura(self, altura: float):
        if altura > 0:
            self.__altura = altura
        else:
            print("Altura inválida!")

    def __str__(self):
        return (
            f"Nome: {self.__nome}\n"
            f"E-mail: {self.__email}\n"
            f"CPF: {self.__cpf}\n"
            f"Idade: {self.__idade}\n"
            f"Altura: {self.__altura:.2f} m"
        )

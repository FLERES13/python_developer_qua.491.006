# superclasse

class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone # private 
        self.__endereco = endereco # private

# métodos de acesso


# método get telefone
    @property
    def telefone(self):
    return self.__telefone


# métodos set telefone
    @telefone.setter        
    def telefone(self, telefone):
        self.__telefone = telefone


    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self__endereco = endereco    

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome 
        self.__cpf = cpf 
        super().__init__(telefone, endereco)
    

    @property
    def nome(self):
    return self.__nome






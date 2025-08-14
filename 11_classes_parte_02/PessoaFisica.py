from dataclasses import dataclass
import Pessoa

@dataclass
class PessoaFisica(Pessoa.Pessoa):
    nome: str
    cpf: str
    idade: int

    def __str__(self):
        return f"{'-'*20} Dados Pessoais: {'-'*20}\n\nNome: {self.nome}\nIdade: {len(self)}\nCPF: {self.cpf}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}"
        
    

    def __len__(self):
        return self.idade




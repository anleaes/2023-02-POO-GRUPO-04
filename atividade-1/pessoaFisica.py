from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, endereço, data_nascimento, cpf):
        super().__init__(nome, telefone, endereço)
        self.data_nascimento = data_nascimento
        self.cpf = cpf 
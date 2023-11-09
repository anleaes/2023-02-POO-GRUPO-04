from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, endereço, anoNascimento, cpf):
        super().__init__(nome, telefone, endereço)
        self.anoNascimento = anoNascimento
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereço}, Data Nascimento: {self.anoNascimento}, CPF: {self.cpf}"
    pass

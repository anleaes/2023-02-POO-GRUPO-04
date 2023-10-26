from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, endereço, cnpj):
        super().__init__(nome, telefone, endereço)
        self.cnpj = cnpj

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereço}, CNPJ: {self.cnpj}"
    pass
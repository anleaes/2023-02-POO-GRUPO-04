from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, cnpj, nome, telefone, endereço):
        super().__init__(nome, telefone, endereço)
        self.cnpj = cnpj
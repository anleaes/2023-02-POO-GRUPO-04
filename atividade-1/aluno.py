from pessoaFisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, telefone, endereço, data_nascimento, cpf, numero_matricula):
         super().__init__(nome, telefone, endereço, data_nascimento, cpf)
         self.numero_matricula = numero_matricula
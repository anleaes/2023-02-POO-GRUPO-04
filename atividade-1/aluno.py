class Aluno:
    def __init__(self, pessoa, cadastro, email):
        self.pessoa = pessoa
        self.cadastro = cadastro
        self.email = email

    def __str__(self):
        return f"Aluno: {self.pessoa}, cadastro: {self.cadastro}, Email: {self.email}"
    pass
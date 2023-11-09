class Inscricao:
    def __init__(self):
        self.alunos = []
    
    def __str__(self):
        return f"Nome: {self.alunos}"
    
    def inscrever_aluno(self, aluno, curso):
        self.alunos.append({"aluno": aluno, "curso": curso})
    pass
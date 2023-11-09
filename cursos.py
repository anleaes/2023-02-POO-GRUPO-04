class Curso:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Nome: {self.nome}, Carga Horária: {self.carga_horaria} horas"
    pass
class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
            return f"\nID: {self.id}, Name: {self.name}, Descrição: {self.description}"
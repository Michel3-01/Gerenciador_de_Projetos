class Colaborador():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email= email
    def print(self):
        print(f'{self.id}, {self.nome} ,{self.email}')
    def get_colaborador(self):
        return[self.nome, self.email]
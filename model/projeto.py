class Projeto():
    def __init__(self, id, nome, descricao):
        self.id = id 
        self.nome = nome
        self.descricao = descricao
    def imprimir(self):
        print(f'{self.id}-{self.nome}-{self.descricao}')

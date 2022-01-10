class ColaboradoresTarefa():
    def __init__(self,id_projeto,id_colaborador,colaborador):
        self.id_projeto = id_projeto
        self.id_colaborador = id_colaborador
        self.colaborador = colaborador
    def print(self):
        print(f'{self.id_projeto}-{self.id_colaborador}-{self.colaborador}')
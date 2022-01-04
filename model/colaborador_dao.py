#Adicionar um novo colaborador.
lista_de_colaboradores = []#Amazena os dados do colaborador.
def adicionar(novo_colaborador):
    lista_de_colaboradores.append(novo_colaborador)
#Editar informações do colaborador.
def getColaborador(id):
    for colaborador in lista_de_colaboradores:
        if colaborador.id == id:
            return colaborador
   

#Excluir um colaborador.
def excluir():
    pass

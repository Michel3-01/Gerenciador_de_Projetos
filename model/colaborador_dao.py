#Adicionar um novo colaborador.
lista_de_colaboradores = []#Amazena os dados do colaborador.
def adicionar(novo_colaborador):
    lista_de_colaboradores.append(novo_colaborador)
#Editar informações do colaborador.
def getColaborador(id):
    for colaborador in lista_de_colaboradores:
        if colaborador.id == id:
            return colaborador
def editar(colaborador):
    for i in range(0,len(lista_de_colaboradores)):
        if colaborador.id == lista_de_colaboradores[i].id:
            lista_de_colaboradores[i]= colaborador

#Excluir um colaborador.
def excluir(colaborador):
    for i in range(0,len(lista_de_colaboradores)):
        if colaborador.id == lista_de_colaboradores[i].id:
            lista_de_colaboradores.remove(colaborador)
#Lista todos os colaboradores.
def listaTodos():
    for colaborador in lista_de_colaboradores:
        colaborador.print()
    



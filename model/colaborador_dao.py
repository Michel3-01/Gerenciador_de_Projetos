#Adicionar um novo colaborador.
lista_de_colaboradores = []#Amazena os dados do colaborador.
def adicionar(novo_colaborador):
    #Inserir o ID do cliente.
    novo_id = len(lista_de_colaboradores)+1
    novo_colaborador.id = novo_id
    #Inserir o colaborador na lista.
    lista_de_colaboradores.append(novo_colaborador)
#Editar informações do colaborador.
def getColaborador(id):
    for colaborador in lista_de_colaboradores:
        if colaborador.id == id:
            return colaborador
def editar(colaborador):
    for i in range(0,len(lista_de_colaboradores)):
        colaborador_atual = lista_de_colaboradores[i]
        if colaborador.id == colaborador_atual.id:
            lista_de_colaboradores[i]= colaborador

#Excluir um colaborador.
def excluir(id_colaborador):
    for index in range(0,len(lista_de_colaboradores)):
        colaborador_atual = lista_de_colaboradores[index]
        if id_colaborador == colaborador_atual.id:
            del lista_de_colaboradores[index]
            return
#Lista todos os colaboradores.
def listaTodos():
    for colaborador in lista_de_colaboradores:
        colaborador.print()
    



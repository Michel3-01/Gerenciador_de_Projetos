#Lista que irá armazena as tarefas.


lista_colaborador_tarefa = []
lista_tarefas = []
#Adicionar um tarefa.
def adicionar(nova_tarefa):
    lista_tarefas.append(nova_tarefa)
#Excluir uma tarefa.
def excluir(id_tarefa):
    for index in range(0,lista_tarefas):
        tarefa_atual = lista_tarefas[index]
        if id_tarefa == tarefa_atual:
            del lista_tarefas[index]
            return
#Pega uma tarefa específica
def PegarTarefa(id_tarefa):
    for tarefa in lista_tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
#Editar uma tarefa.
def editar(tarefa):
    for index in range(0,len(lista_tarefas)):
        tarefa_atual = lista_tarefas[index]
        if tarefa.id == tarefa_atual.id:
            lista_tarefas[index] = tarefa
# Lista todas as tarefas.
def listarTarefas():
    for tarefa in lista_tarefas:
        tarefa.print()
def adicionar_colaboradores(id_tarefa,colaborador):
    for index in range(0,len(lista_tarefas)):
        tarefa_atual = lista_tarefas[index]
        if id_tarefa == tarefa_atual.id:
            lista_colaborador_tarefa.append(colaborador)
            
def listaColaboradoresTarefa(id_tarefa):
    for index in range(0,len(lista_tarefas)):
        tarefa_atual = lista_tarefas[index]
        if id_tarefa == tarefa_atual.id:
            for colaboradores in lista_colaborador_tarefa:
                colaboradores.print()
                





from model.tabela_dao import lista_tarefas
lista_colaborador_tarefa = []

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
                


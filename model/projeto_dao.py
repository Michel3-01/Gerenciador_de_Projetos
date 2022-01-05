#Lista que armazena os projetos.
lista_projetos = []
#Adiciona um novo Projeto.
def adicionar(novo_projeto):
    lista_projetos.append(novo_projeto)
def editar(projeto):
    for index in range(0,len(lista_projetos)):
        projeto_atual = lista_projetos[index]
        if projeto.id == projeto_atual.id:
            lista_projetos[index] = projeto
        
def excluir(id_projeto):
    for index in range(0,len(lista_projetos)):
        projeto_atual = lista_projetos[index]
        if id_projeto == projeto_atual.id:
            del lista_projetos[index]
            return
def listarProjetos():
    for projetos in lista_projetos:
        projetos.imprimir()

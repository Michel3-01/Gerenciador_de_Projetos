from model.colaborador import Colaborador
from qt_core import *
from controller.main_window import MainWindow
import model.colaborador_dao as funções_colaborador
from model.projeto import Projeto
import model.projeto_dao as funções_projeto
import model.tabela_dao as funções_tarefas
from model.tarefa import Tarefa
from model.colaborador_tarefa import ColaboradoresTarefa
import model.colaborador_tarefa_dao as funções_colaborador_tarefa
#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#sys.exit(app.exec())
for i in range(0,3):   
    novo_colaborador= Colaborador(i,f'Colaborador{i}','Almeida@gmail.com')
    funções_colaborador.adicionar(novo_colaborador)
print(40*"-")
print("Lista de todos os colaboradores.")
funções_colaborador.listaTodos()
funções_colaborador.excluir(7)
funções_colaborador.excluir(3)
print(40*"-")
print("Apos a exclusão do 10 e 3.")
funções_colaborador.listaTodos()

#get_id = getColaborador(9)
#get_id.print()
#get_id.nome = 'Michele Almeida'
#get_id.print()
#get_id.email="Rua do Capiroto"
#editar(get_id)
#get_id.print()
#listaTodos()
#colaborador = 1
#excluir(colaborador)
#listaTodos()
index = 8
novo_projeto = Projeto(index,'Aprender inglês','Aprender a lingua inglesa, bla bla bla.')
novo_projeto01 = Projeto(9,'blabla',"bla bla bla")
funções_projeto.adicionar(novo_projeto01)
funções_projeto.adicionar(novo_projeto)
print("Lista de todos os projetos.")
funções_projeto.listarProjetos()
funções_projeto.excluir(9)
print(30*"-")
funções_projeto.listarProjetos()
funções_projeto.excluir(8)
print(30*"-")
funções_projeto.listarProjetos()
print("Nenhum projeto encontrado.")

print("Adicionando uma colaborador a uma tarefa")
for x in range(0,3):
    nova_tarefa = Tarefa(x,"bla bla bla","Concluído")
    funções_tarefas.adicionar(nova_tarefa)

for x in range(0,3):
    novo_projeto = Projeto(x,f'Projeto{x}','Descrição{x}')
    funções_projeto.adicionar(novo_projeto)

funções_projeto.listarProjetos()
funções_tarefas.listarTarefas()
colaborador = Colaborador(1,'michele',"Almeida@gmeil.com")
#colaborador01 = Colaborador(1,'João',"Joãosilva45@gmail.com")
#funções_tarefas.adicionar_colaboradores(1,colaborador)
#funções_tarefas.adicionar_colaboradores(1,colaborador01)
#funções_tarefas.listaColaboradoresTarefa(1)
print("Lista de colaboradores por tarefa")
pegar_colaborador = funções_colaborador.getColaborador(1)
pegar_projeto = funções_projeto.pegarProjeto(1)
pegar_tarefa = funções_tarefas.PegarTarefa(2)
colaborador_tarefa = ColaboradoresTarefa(pegar_projeto.print(),pegar_tarefa,pegar_colaborador)
print("Adicionando colaborado.")
funções_colaborador_tarefa.adicionar_colaboradores(1,colaborador_tarefa)

funções_colaborador_tarefa.listaColaboradoresTarefa(1)










from model.colaborador import Colaborador
from qt_core import *
from controller.main_window import MainWindow
import model.colaborador_dao as funções_colaborador
from model.projeto import Projeto
import model.projeto_dao as funções_projeto

#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#sys.exit(app.exec())
for i in range(0,10):   
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
novo_projeto = Projeto(index,'Aprender inglês','Aprender a lingua inglesa, pois isso ajudará a consiguir vagas no mercado de trabalho.')
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




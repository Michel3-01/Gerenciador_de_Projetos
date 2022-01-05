from model.colaborador import Colaborador
from qt_core import *
from controller.main_window import MainWindow
from model.colaborador_dao import *

#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#sys.exit(app.exec())
for i in range(0,10):   
    novo_colaborador= Colaborador(i,f'Colaborador{i}','Almeida@gmail.com')
    adicionar(novo_colaborador)


get_id = getColaborador(9)
get_id.print()
get_id.nome = 'Michele Almeida'
get_id.print()
get_id.email="Rua do Capiroto"
editar(get_id)
get_id.print()
listaTodos()
colaborador = 9
excluir(colaborador)
listaTodos()



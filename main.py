from model.colaborador import Colaborador
from qt_core import *
from controller.main_window import MainWindow
from model.colaborador_dao import *

#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#sys.exit(app.exec())

novo_colaborador= Colaborador(1,'Marcos','Almeida@gmail.com')
adicionar(novo_colaborador)

get_id = getColaborador(1)
get_id.print()
get_id.nome = 'Michele Almeida'
get_id.print()

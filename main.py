#Classe PRincipal
from qt_core import *
from controller.main_window import MainWindow
from controller.projeto_page import ProjetoPage
from controller.colaborador_page import ColaboradorPage

app = QApplication(sys.argv)

window =ColaboradorPage()
window.show()
app.exec()
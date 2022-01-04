from qt_core import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui',self)

        self.Show_Gerenciador_de_Tarefas_Page()

    def Show_Gerenciador_de_Tarefas_Page(self):
        self.painel_principal.setCurrentIndex(0)
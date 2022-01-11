from qt_core import *
from controller.colaborador_page import ColaboradorPage
from controller.projeto_page import ProjetoPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui',self)
        #Criar os objetos das páginas.
        self.colabodor_page = ColaboradorPage()
        self.projeto_page = ProjetoPage()

        #Adiciona às páginas ao painel principal.
        self.painel_principal.insertWidget(0,self.colabodor_page)
        self.painel_principal.insertWidget(1,self.projeto_page)
    
        #Colocar os eventos dos botões
        self.novoprojeto_btn.clicked.connect(self.show_projeto)
        self.colaborador_btn.clicked.connect(self.show_colaborador)

    def show_projeto(self):
        self.painel_principal.setCurrentIndex(1)

    def show_colaborador(self):
        self.painel_principal.setCurrentIndex(0)

        

   
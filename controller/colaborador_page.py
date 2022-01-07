#Classe que irá controlar o arquivo colaboradores_page.ui.
from qt_core import *
#Arquivo colaboradores_page.ui
FILE_UI = "view/colaboradores_page.ui"

class ColaboradorPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
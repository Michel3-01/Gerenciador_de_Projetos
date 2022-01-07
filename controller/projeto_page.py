#Classe que irá controlar o arquivo projeto_page.ui.
from PyQt5.uic.uiparser import QtWidgets
from qt_core import *
#Arquivo projeto_page.ui.
FILE_UI = "view/projeto_page.ui"
class ProjetoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        
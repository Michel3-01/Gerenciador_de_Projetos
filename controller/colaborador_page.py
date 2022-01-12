#Classe que irá controlar o arquivo colaboradores_page.ui.
from model.colaborador import Colaborador
from qt_core import *
import model.colaborador_dao as funções_colaborador
#Arquivo colaboradores_page.ui
FILE_UI = "view/colaboradores_page.ui"

class ColaboradorPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
    #Evento dos botões da página colaboradores.
        self.excluir_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
    
    def fechar_janela(self):#Função de fechar a janela.
        self.close()
    def salvar(self):
        #Pega os dados dos colaboradores.
        nome = self.campo_nome.text()
        email = self.campo_email.text()

        #Cria o objeto
        novo_colaborador = Colaborador(0,nome,email)
        funções_colaborador.adicionar(novo_colaborador)
        funções_colaborador.listaTodos()

        #Atualizar a tabela.
        self.carrega_dados()
        #Fechar a janela.
        self.close()
    #Carrega os dados na minha tabela.
    def carrega_dados(self):
        #Pegar a lista de colaboradores.
        lista_colaboradores = funções_colaborador.lista_de_colaboradores
        #Zera a tabela -ir para a linha zero.
        self.tabela.setRowCount(0)
        #Adicionar os elementos na tabela.
        for colaborador in lista_colaboradores:
            self.add_linha(colaborador)
    
    def add_linha(self,colaborador):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)
    
        #Elemento de cada coluna da tabela.
        id = QTableWidgetItem(str(colaborador.id))
        nome = QTableWidgetItem(colaborador.nome)
        email = QTableWidgetItem(colaborador.email)

        #Inseri os elementos na tabela na coluna correspondente.
        #(linha, coluna, item).
        self.tabela.setItem(rowCount,0,id)
        self.tabela.setItem(rowCount,1,nome)
        self.tabela.setItem(rowCount,2,email)
#IMPORTANDO AS BIBLIOTECAS
#from mhyt import yt_download
from frame import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

#AQUI ESTAMOS CRIANDO UMA CLASSE MAIN WINDOW E HERDANDO AS PROPRIEDADES DO NOSSO ARQUIVO FRAME.PY(NOSSA JANELA)
class MainWindow(QMainWindow,Ui_MainWindow):
#AQUI INICIAMOS COM O NOSSO MÉTODO CONSTRUTOR DA CLASSE, É AQUI QUE VAMOS COLOCAR OS ELEMENTOS E FUNÇÕES DE CADA UM)
    def __init__(self):#MÉTODO CONSTRUTOR
        super(MainWindow, self).__init__()# AQUI ESTAMOS USANDO O METODO SUPER PARA HERDAR TUDO NA CLASSE MAIN WINDOW
        self.setupUi(self)#AQUI ESTAMOS PUXANDO TODAS AS CONFIGURAÇÕES DE NOSSA JANELA
        self.setWindowTitle("YouTube Download")#AQUI ESTAMOS COLOCANDO O TITULO DE NOSSA JANELA
        appIcon = QIcon("YouTub-icon.png")
        self.setWindowIcon(appIcon)
        self.download.clicked.connect(self.Download)#AQUI ESTAMOS COLOCANDO O NOSSO BOTÃO DOWNLOAD PARA FAZER UMA CONEXÃO COM UMA FUNÇÃO
        self.link.text()#CAMPO PARA COLOCAR O LINK
        self.titulo.text()#CAMPO PARA COLOCAR O TÍTULO
        self.mp4.isChecked()#RADIOBUTTON PARA SELECIONAR O FORMATO MP4
        self.mp3.isChecked()#RADIOBUTTON PARA SELECIONAR O FORMATO MP3

    def Download(self):#METODO PARA FAZER O DOWNLOAD DO VIDEO
        if self.mp4.isChecked() == True:#SE O RADIOBUTTON MP4 ESTIVER CLICKADO, ENTÃO EXECUTE AS LINHAS ABAIXO
            link = self.link.text()# INSIRA O LINK
            título = self.titulo.text()# INSIRA UM TITULO
            título_mp4 = título + '.mp4'# O TITULO MP4 VAI SER IGUAL AO TITULO + EXTENSÃO
            yt_download(link, título_mp4)# FUNÇÃO PARA BAIXAR O ARQUIVO EM MP4
        elif self.mp3.isChecked() == True:# O TITULO MP4 VAI SER IGUAL AO TITULO + EXTENSÃO
            try:#TENTE
                link = self.link.text()# INSIRA O LINK
                título = self.titulo.text()# INSIRA UM TITULO
                título_mp3 = título + '.mp3'# O TITULO MP3 VAI SER IGUAL AO TITULO + EXTENSÃO
                yt_download(link, título_mp3, ismusic=True, codec="mp3")#FUNÇÃO PARA BAIXAR O ARQUIVO EM MP4
            except:#SE TIVER EXCEÇÃO
                pass #PASSE

if __name__ == "__main__":#EXECUTE TODAS AS LINHAS ACIMA, MENOS OS ITENS DESCRITOS ABAIXO
    app = QApplication(sys.argv)#APP DEFINIDO
    window = MainWindow()#JANELA
    window.show()#MOSTRAR JANELA
    app.exec_()#EXECUTAR O APP

import sys
#Importamos los modulos de pyqt5 que necesitamos
from PyQt5.QtWidgets import QDialog, QApplication
#Importamos el archivo compilado de la ventana
from login import *

#Hacemos que herede de QDialog
class Login(QDialog):
    def __init__(self):
        #Iniciamos el constructor de QDialog
        super().__init__()
        #Instanciamos un objeto de saludo.py
        self.login = Ui_Login()
        #Iniciamos la interfaz
        self.login.setupUi(self)
        #Mostramos el dialogo
        self.show()

#Creamos la Aplicacion con la instancia de QApplication
if __name__ == '__main__':
    #Creamos la instancia de QApplication con los argumentos que pide
    #Creamos el entorno
    app = QApplication(sys.argv)
    #Creamos el dialogo
    dialogo = Login()
    #Mostramos
    dialogo.show()
    #Evento de salida
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from img import img
import sys

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(961, 609)
        Login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Login.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(0, 0, 961, 611))
        self.frame.setStyleSheet("border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Imagen = QtWidgets.QLabel(self.frame)
        self.Imagen.setGeometry(QtCore.QRect(0, 0, 961, 611))
        self.Imagen.setStyleSheet("border-image: url(:/img/login.jpeg);\n"
"border-radius: 20px;")
        self.Imagen.setText("")
        self.Imagen.setObjectName("Imagen")
        self.sombraImagen = QtWidgets.QLabel(self.frame)
        self.sombraImagen.setGeometry(QtCore.QRect(0, 0, 961, 611))
        self.sombraImagen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius: 20px;\n"
"background-color: rgba(0,0,0,50);")
        self.sombraImagen.setText("")
        self.sombraImagen.setObjectName("sombraImagen")
        self.sombraLogin = QtWidgets.QLabel(self.frame)
        self.sombraLogin.setGeometry(QtCore.QRect(60, 60, 831, 501))
        self.sombraLogin.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius: 20px;")
        self.sombraLogin.setText("")
        self.sombraLogin.setObjectName("sombraLogin")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_4.setObjectName("label_4")
        self.txtUsuario = QtWidgets.QLineEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(280, 230, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:  none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 255);;\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px;")
        self.txtUsuario.setText("")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtContrasenia = QtWidgets.QLineEdit(self.frame)
        self.txtContrasenia.setGeometry(QtCore.QRect(280, 370, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtContrasenia.setFont(font)
        self.txtContrasenia.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:  none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 255);;\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px;")
        self.txtContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtContrasenia.setObjectName("txtContrasenia")
        self.btnSalir = QtWidgets.QPushButton(self.frame)
        self.btnSalir.setGeometry(QtCore.QRect(280, 480, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet("background-color: rgb(181, 0, 3,60%);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px;")
        self.btnSalir.setObjectName("btnSalir")
        self.btnIngresar = QtWidgets.QPushButton(self.frame)
        self.btnIngresar.setGeometry(QtCore.QRect(510, 480, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("background-color: rgb(29, 89, 185, 60%);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px;")
        self.btnIngresar.setObjectName("btnIngresar")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_4.setText(_translate("Login", "Agroquímicos \"La Huerta\""))
        self.txtUsuario.setPlaceholderText(_translate("Login", "Usuario"))
        self.txtContrasenia.setPlaceholderText(_translate("Login", "Contraseña"))
        self.btnSalir.setText(_translate("Login", "Salir"))
        self.btnIngresar.setText(_translate("Login", "Ingresar"))
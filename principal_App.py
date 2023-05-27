import sys
#Importamos los modulos de pyqt5 que necesitamos
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
#Importamos el archivo compilado de la ventana
from principal import *


class Principal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnMenu.clicked.connect(self.moverBarra)
        self.ui.btnNuevaVenta.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageVenta))



    # Movemos la barra lateral, además de los formularios que contienen los botones
    def moverBarra(self):
        if True:
            width = self.ui.frmBarraLateral.width()
            normal = 350
            if width == 350:
                extender = 70
                extender2 = 0
            else:
                extender = normal
                extender2 = normal

        # Movemos la barra completa
        self.animacionBarraGeneral = QPropertyAnimation(self.ui.frmBarraLateral, b'minimumWidth')
        self.animacionBarraGeneral.setDuration(300)
        self.animacionBarraGeneral.setStartValue(width)
        self.animacionBarraGeneral.setEndValue(extender)
        self.animacionBarraGeneral.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionBarraGeneral.start()

        # Movemos cada una de las secciones
        self.animacionProductos = QPropertyAnimation(self.ui.frmProductos, b'minimumWidth')
        self.animacionProductos.setDuration(450)
        self.animacionProductos.setStartValue(width)
        self.animacionProductos.setEndValue(extender2)
        self.animacionProductos.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionProductos.start()

        self.animacionVentas = QPropertyAnimation(self.ui.frmVentas, b'minimumWidth')
        self.animacionVentas.setDuration(450)
        self.animacionVentas.setStartValue(width)
        self.animacionVentas.setEndValue(extender2)
        self.animacionVentas.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionVentas.start()

        self.animacionEmpleados = QPropertyAnimation(self.ui.frmEmpleados, b'minimumWidth')
        self.animacionEmpleados.setDuration(450)
        self.animacionEmpleados.setStartValue(width)
        self.animacionEmpleados.setEndValue(extender2)
        self.animacionEmpleados.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionEmpleados.start()

        self.animacionSalir = QPropertyAnimation(self.ui.frmSalir, b'minimumWidth')
        self.animacionSalir.setDuration(450)
        self.animacionSalir.setStartValue(width)
        self.animacionSalir.setEndValue(extender2)
        self.animacionSalir.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionSalir.start()


# Creamos la aplicación, iniciamos y definimos el método de salida
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Principal()
    w.show()
    sys.exit(app.exec_())
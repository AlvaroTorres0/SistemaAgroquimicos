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

        self.animacionBarraGeneral = QPropertyAnimation(self.ui.frmBarraLateral, b'minimumWidth')
        self.animacionBarraGeneral.setDuration(300)
        self.animacionBarraGeneral.setStartValue(width)
        self.animacionBarraGeneral.setEndValue(extender)
        self.animacionBarraGeneral.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionBarraGeneral.start()

        self.animacionFrmProductos = QPropertyAnimation(self.ui.frmProductos, b'minimumWidth')
        self.animacionFrmProductos.setDuration(450)
        self.animacionFrmProductos.setStartValue(width)
        self.animacionFrmProductos.setEndValue(extender2)
        self.animacionFrmProductos.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionFrmProductos.start()

        self.animacionFrmEmpleados = QPropertyAnimation(self.ui.frmEmpleados, b'minimumWidth')
        self.animacionFrmEmpleados.setDuration(450)
        self.animacionFrmEmpleados.setStartValue(width)
        self.animacionFrmEmpleados.setEndValue(extender2)
        self.animacionFrmEmpleados.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionFrmEmpleados.start()

        self.animacionFrmVentas = QPropertyAnimation(self.ui.frmVentas, b'minimumWidth')
        self.animacionFrmVentas.setDuration(450)
        self.animacionFrmVentas.setStartValue(width)
        self.animacionFrmVentas.setEndValue(extender2)
        self.animacionFrmVentas.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionFrmVentas.start()

        self.animacionFrmSalir = QPropertyAnimation(self.ui.frmSalir, b'minimumWidth')
        self.animacionFrmSalir.setDuration(450)
        self.animacionFrmSalir.setStartValue(width)
        self.animacionFrmSalir.setEndValue(extender2)
        self.animacionFrmSalir.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionFrmSalir.start()




# Creamos la aplicación, iniciamos y definimos el método de salida
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Principal()
    w.show()
    sys.exit(app.exec_())
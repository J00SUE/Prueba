from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.uic import loadUi
from Modelo import Paciente

class VentanaPpal(QMainWindow):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("ventana_pp.ui", self)
        self.setup()
        self.__controlador = None

    def setControlador(self, controlador):
        self.__controlador = controlador

    def setup(self):
        self.Usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.Contra.setValidator(QIntValidator())

        self.Ingreso.clicked.connect(self.abrir_ventana_ingresar)
        #self.Salir.clicked.connect(self.opcionCancelar)

    def abrir_ventana_ingresar(self):
        ventana_ingreso = VentanaIngreso(self)
        self.hide()
        ventana_ingreso.show()

    def opcionCancelar(self):
        self.__ventanaPadre.show()

class VentanaIngreso(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("ventana_ingreso.ui", self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.Boton.clicked.connect(self.abrir_ventana_ingreso)
        #self.Salir.rejected.connect(self.opcionCancelar)

    def abrir_ventana_ingreso(self):
        ventana_ingreso = Ingresar(self)
        self.hide()
        ventana_ingreso.show()

    def opcionCancelar(self):
        self.__ventanaPadre.show()

class Ingresar(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("Ingresar.ui", self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.Nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.Apellido.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.CC.setValidator(QIntValidator())
        self.Edad.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcionAceptar)
        self.buttonBox.rejected.connect(self.opcionCancelar)

    def opcionAceptar(self):
        n = self.Nombre.text()
        a = self.Apellido.text()
        c = int(self.CC.text())
        e = int(self.Edad.text())
        self.__ventanaPadre.recibir_info(n, a, c, e)
        self.__ventanaPadre.show()

    def opcionCancelar(self):
        self.__ventanaPadre.show()

    
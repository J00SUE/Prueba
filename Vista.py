import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaPpal(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_pp.ui",self)
        self.setup()

    def setup(self):
        self.Usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.Contra.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        
        r = self.Usuario.text()
        f = self.Contra.text()
        self.__ventanaPadre.recibir_info(r,f)
        self.__ventanaPadre.show()

        if True:
            self.clicked.connect(self.abrir_ventana_ingresar)


    def abrir_ventana_ingresar(self):
            ventana_aumetar= VentanaIngreso(self)
            self.hide()
            ventana_aumetar.show()

class VentanaIngreso(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_ingreso.ui",self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.Boton.accepted.connect(self.abrir_ventana_ingreso)
        self.Salir.rejected.connect(self.opcionCancelar)
    
    def abrir_ventana_ingreso(self):
        ventana_aumetar= Ingresar(self)
        self.hide()
        ventana_aumetar.show()

    def opcionCancelar(self):
        self.__ventanaPadre.show()

class Ingresar(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Ingresar.ui",self)
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
        r = self.Nombre.text()
        f = self.Apellido.text()
        c = self.CC.text()
        e = self.Edad.text()
        self.__ventanaPadre.recibir_info(r,f,c,e)
        self.__ventanaPadre.show()

    def opcionCancelar(self):
        self.__ventanaPadre.show()

    
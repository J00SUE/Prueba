from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.uic import loadUi
import json
import os
from Modelo import Paciente
from Modelo import Sistema
S = Sistema()

class VentanaPpal(QMainWindow):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("ventana_pp.ui", self)
        self.setup()
        self.__controlador = None

    def setControlador(self, controlador):
        self.__controlador = controlador

    def setup(self):
        self.Ingreso.clicked.connect(self.abrir_ventana_ingresar)
        self.Salir.clicked.connect(self.opcionCancelar)
        self.Usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z0-9]+")))
        self.Contra.setValidator(QRegExpValidator(QRegExp("[a-zA-Z0-9]+")))

    def abrir_ventana_ingresar(self):
        a = self.Usuario.text()
        b = self.Contra.text()
        if a == "admin123":
            if b == "contrasena123":
                ventana_ingreso = VentanaIngreso(self)
                self.hide()
                ventana_ingreso.show()
            else:
                QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos. Por favor, intente de nuevo.")

        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos. Por favor, intente de nuevo.")

    def opcionCancelar(self):
        QApplication.quit()

class VentanaIngreso(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("ventana_ingreso.ui", self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.Boton.clicked.connect(self.abrir_ventana_ingreso)
        self.Salir.clicked.connect(self.opcionCancelar)

    def abrir_ventana_ingreso(self):
        ventana_ingreso = Ingresar(self)
        self.hide()
        ventana_ingreso.show()

    def opcionCancelar(self):
        self.hide()
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
        self.Nombre_b.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.buttonBox.accepted.connect(self.opcionAceptar)
        self.buttonBox.rejected.connect(self.opcionCancelar)
        self.Buscar.clicked.connect(self.buscar)


    def opcionAceptar(self):
        n = self.Nombre.text()  # Nombre
        a = self.Apellido.text()  # Apellido
        c = int(self.CC.text())  # CC
        e = int(self.Edad.text())  # Edad




        data = {}


        try:
            with open('pacientes.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:

            pass


        data[c] = {
            "Nombre": n,
            "Apellido": a,
            "Edad": e
        }

        # Guardamos el diccionario en un archivo JSON
        archivo = 'pacientes.json'
        with open(archivo, 'w') as file:
            json.dump(data, file, indent=4)

        self.__ventanaPadre.show()

    def buscar(self):
    
        Name = self.Nombre_b.text()
        T = S.buscarPorNombre(Name)
        self.label_5.setText(T)


    def opcionCancelar(self):
        self.__ventanaPadre.show()

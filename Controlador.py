from Modelo import *
from Vista import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 

class Coordinador:
    def __init__(self, vista, modelo):
        self.__miVista = vista
        self.__miModelo = modelo

    def recibir_usu(self, n, r):
        if self.__miModelo.verificar(n, r):
            return self.__miModelo
        else:
            return "Error"

    def recibir_info(self, n, r, f, c, e):
        self.__miModelo.agregarpaciente(n, r, f, c, e)

def main():
    app = QApplication(sys.argv)
    mi_modelo = Sistema()
    mi_vista = VentanaPpal()
    mi_controlador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
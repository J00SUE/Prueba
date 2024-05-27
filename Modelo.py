class Admin():
    def __init__(self):
        self.__usuario = ""
        self.__contraseña = ""

    def aggUsuario(self, usuario):
        self.__usuario = usuario

    def aggContraseña(self, contraseña):
        self.__contraseña = contraseña

    def verUsuario(self):
        return self.__usuario
    
    def verContraseña(self):
        return self.__contraseña
    
class Paciente():
    def __init__(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__edad = 0
        self.__cc = 0

    def aggnombre(self, nombre):
        self.__nombre = nombre

    def aggapellido(self, apellido):
        self.__apellido = apellido

    def aggedad(self, edad):
        self.__edad = edad

    def aggcc(self, cc):
        self.__cc = cc

    def vernombre(self):
        return self.__nombre
    
    def verapellido(self):
        return self.__apellido
    
    def veredad(self):
        return self.__edad
    
    def vercc(self):
        return self.__cc
    
class Sistema():
    def __init__(self):
        self.__credenciales = {}
        self.__credenciales["admin"] = "123"
        self.__paciente = {}
        A = False

    def verificar(self, usuario, contraseña):
        if usuario in self.__credenciales:  
            if contraseña == self.__credenciales[usuario]:  
                A = True
                return A
            else:
                return A
        else:
            return A
        
    def agregarpaciente(self,n,a,e,c):
        p = Paciente()
        p.aggnombre(n)
        p.aggapellido(a)
        p.aggedad(e)
        p.aggcc(c)
        self.__paciente[p.vercc()] = p

    def verificarExiste(self,clave):
        return clave in self.__paciente
        

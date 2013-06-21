#Clase
class Coche:
    def __init__(self,  gasolina):
        self.gasolina = gasolina
        print "Tenemos",  gasolina,  "litros"

    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve"

#Herencia
class Terrestre:
    def desplazar(self):
        print "El animal anda"

class Acuatico:
    def nadar(self):
        print "El animal nada"

class Cocodrilo(Terrestre, Acuatico):
    pass

#Encapsulamiento
class Ejemplo:
    def publico(self):
        print "Publico"
    def __privado(self):
        print "Privado"

class Fecha(object):
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print "Error"
    dia = property(getDia, setDia)
